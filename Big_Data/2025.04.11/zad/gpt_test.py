import os

def get_all_files_in_directory(directory):
    return [entry.name for entry in os.scandir(directory) if entry.is_file()]


from PIL import Image

def average_RGB_from_image(img_path):
    img = Image.open(img_path)
    pixels = img.load()
    cols, rows = img.size

    r = g = b = 0
    total_pixels = cols * rows

    for x in range(cols):
        for y in range(rows):
            r_px, g_px, b_px = pixels[x, y]
            r += r_px
            g += g_px
            b += b_px

    return (r // total_pixels, g // total_pixels, b // total_pixels)

import multiprocessing
import time

def worker_avg_rgb(img_name, img_dir, result_list):
    path = os.path.join(img_dir, img_name)
    avg = average_RGB_from_image(path)
    result_list.append((img_name, *avg))

def calc_avg_rgb_for_images(images_directory, output_file="rgb.txt"):
    start = time.time()
    manager = multiprocessing.Manager()
    results = manager.list()
    images = get_all_files_in_directory(images_directory)
    
    processes = []
    for img_name in images:
        p = multiprocessing.Process(target=worker_avg_rgb, args=(img_name, images_directory, results))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    with open(output_file, "w") as f:
        for name, r, g, b in results:
            f.write(f"{name};{r};{g};{b}\n")

    print(f"Obliczono średnie RGB w {(time.time() - start):.2f} s")

def load_rgb_data(file_path="rgb.txt"):
    data = []
    with open(file_path, "r") as f:
        for line in f:
            name, r, g, b = line.strip().split(";")
            data.append((name, int(r), int(g), int(b)))
    return data

def main_image_to_tiles(img_path, tile_size):
    img = Image.open(img_path)
    pixels = img.load()
    cols, rows = img.size

    tiles = []
    for i in range(cols // tile_size):
        tiles.append([])
        for j in range(rows // tile_size):
            r = g = b = 0
            for x in range(tile_size):
                for y in range(tile_size):
                    rx, gx, bx = pixels[i*tile_size + x, j*tile_size + y]
                    r += rx
                    g += gx
                    b += bx
            total = tile_size * tile_size
            avg = (r // total, g // total, b // total)
            tiles[i].append(avg)
    return tiles

from scipy.spatial import KDTree

def build_kdtree(rgb_data):
    colors = [(r, g, b) for _, r, g, b in rgb_data]
    tree = KDTree(colors)
    return tree, colors

def find_images_for_column(pixels, rgb_data, tree, images_directory, c, pipe):
    results = []
    for pixel in pixels:
        dist, index = tree.query(pixel)
        img_name = rgb_data[index][0]
        img_path = os.path.join(images_directory, img_name)
        results.append(img_path)
    pipe.send((results, c))

def join_images(tiles_pixels, images_directory, rgb_data, tile_size=150):
    from multiprocessing import Process, Pipe

    tree, _ = build_kdtree(rgb_data)
    cols = len(tiles_pixels)
    rows = len(tiles_pixels[0])

    new_img = Image.new("RGB", (cols * tile_size, rows * tile_size))
    workers = []
    pipes = []

    for c in range(cols):
        parent, child = Pipe()
        p = Process(target=find_images_for_column, args=(tiles_pixels[c], rgb_data, tree, images_directory, c, child))
        workers.append(p)
        pipes.append(parent)
        p.start()

    for p in workers:
        p.join()

    for pipe in pipes:
        images_paths, c = pipe.recv()
        for r, path in enumerate(images_paths):
            # tile_img = Image.open(path).resize((tile_size, tile_size))
            tile_img = Image.open(path)
            new_img.paste(tile_img, (c * tile_size, r * tile_size))

    new_img.save("final_img.png", format="PNG", compress_level=0)
    print("Zapisano finalny obraz jako 'final_img.png'")

def main():
    images_directory = "seg_pred"
    main_img_path = "fotka04.png"
    tile_size = 150

    begin = time.time()
    calc_avg_rgb_for_images(images_directory)
    rgb_data = load_rgb_data()

    tiles = main_image_to_tiles(main_img_path, 1)  # 8x8 pikseli – potem każdy zamieniany na obrazek 150x150

    join_images(tiles, images_directory, rgb_data, tile_size=tile_size)
    end = time.time()

    print(f"{end-begin} s")

if __name__ == "__main__":
    main()
