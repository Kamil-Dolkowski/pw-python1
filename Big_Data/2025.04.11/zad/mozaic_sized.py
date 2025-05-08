# https://fulmanski.pl/zajecia/big_data/zajecia_20212022/projects.php
# 3 zbiór (150 x 150 px)

# przeskalowanie katalogu
# średnie RGB dla każdego z obrazków
# zapis do pliku/bazy danych
# zamiana pikseli głównego obrazka na obrazki

import os
from PIL import Image
import multiprocessing
from multiprocessing import Pipe
import time
import sys


def get_all_images_in_directory(directory):
    image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp'}
    images = []

    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)

        if not os.path.isdir(file_path) and any(file.lower().endswith(ext) for ext in image_extensions):
            images.append(file)

    return images

def average_rgb_from_image(img_name, img_directory, tSize):
    img_path = os.path.join(img_directory, img_name)

    img = Image.open(img_path)
    img = img.convert("RGB")
    pixels = img.load()
    cols, rows = img.size

    left = (cols // 2) - (tSize // 2)
    top = (rows // 2) - (tSize // 2)
    right = left + tSize
    bottom = top + tSize

    if (left < 0 or top < 0 or right > cols or bottom > rows):
        sys.stdout.write(f"\r(!) Ostrzeżenie: Zdjęcie '{img_name}' ma za mały rozmiar.")
        sys.stdout.write(f"\nLiczenie średnich RGB: ")
        sys.stdout.flush()

    # print(f"{left}, {top}, {right}, {bottom}")

    cropped_img = img.crop((left, top, right, bottom))

    pixels = cropped_img.load()
    cols, rows = cropped_img.size

    s = cols * rows

    r, g, b = (0,0,0)

    for x in range(cols):
        for y in range(rows):
            rPx, gPx, bPx = pixels[x, y]

            r += rPx
            g += gPx
            b += bPx

    r = (int)(r/s)
    g = (int)(g/s)
    b = (int)(b/s)
            
    # return (r,g,b)
    with open("rgb.txt", "a") as file:
        file.write(f"{img_name};{r};{g};{b}\n")

def calc_avg_rgb_for_images(images_directory, tSize):
    print("Liczenie średnich RGB:", end=" ")
    begin = time.time()
    with open("rgb.txt", "w") as file:
        file.write("")

    images = get_all_images_in_directory(images_directory)
    workers = []

    for image in images:
        worker = multiprocessing.Process(target=average_rgb_from_image, args=(image, images_directory, tSize))
        workers.append(worker)
        worker.start()

    for worker in workers:
        worker.join()

    end = time.time()
    print(f"100% [{(end-begin):.1f}s]")

def main_image_to_tiles(img_name, tSize):
    img = Image.open(img_name)
    img = img.convert("RGB")
    pixels = img.load()
    cols, rows = img.size

    tiles_pixels = []
    for i in range((int)(cols/tSize)):
        tiles_pixels.append([])

        for j in range((int)(rows/tSize)):
            tiles_pixels[i].append((0,0,0))

    s = tSize * tSize

    for i in range((int)(cols/tSize)):
        for j in range((int)(rows/tSize)):

            r, g, b = (0,0,0)

            for x in range(tSize):
                for y in range(tSize):
                    rPx, gPx, bPx = pixels[i*tSize+x, j*tSize+y]

                    r += rPx
                    g += gPx
                    b += bPx

            r = (int)(r/s)
            g = (int)(g/s)
            b = (int)(b/s)

            for x in range(tSize):
                for y in range(tSize):
                    pixels[i*tSize+x, j*tSize+y] = (r,g,b)

            tiles_pixels[i][j] = (r,g,b)
    return tiles_pixels

def join_images(tiles_pixels, images_directory, final_image, tSize = 150):
    workers = []
    pipes = []
    rows, cols = len(tiles_pixels) * tSize, len(tiles_pixels[0]) * tSize

    new_image = Image.new("RGB", (rows, cols))

    print("Szukanie odpowiednich zdjęć:", end=" ")
    begin = time.time()

    for r in range(int(rows/tSize)):
        pipeParent, pipeChild = Pipe()

        worker = multiprocessing.Process(
            target = find_suitable_images_for_pixels_in_rows, 
            args = (tiles_pixels[r], images_directory, r, pipeChild)
        )
        workers.append(worker)
        pipes.append(pipeParent)
        worker.start()
        
    
    for worker in workers:
        worker.join()
        
    end = time.time()
    print(f"100% [{(end-begin):.1f}s]")


    print("Łączenie zdjęć:", end=" ")
    begin = time.time()

    number_of_rows = len(pipes)
    row_number = 1

    for p in pipes:
        images_paths,r = p.recv()

        c = 0
        for img_path in images_paths:
            
            image = Image.open(img_path)

            # image = image.convert("RGB")
            cols, rows = image.size

            left = (cols // 2) - (tSize // 2)
            top = (rows // 2) - (tSize // 2)
            right = left + tSize
            bottom = top + tSize

            cropped_img = image.crop((left, top, right, bottom))

            new_image.paste(cropped_img,(r*tSize,c*tSize))

            c+=1
        sys.stdout.write(f'\rŁączenie zdjęć: {int(100 * row_number/number_of_rows)}%')
        sys.stdout.flush()
        row_number += 1
    
    end = time.time()
    print(f" [{(end-begin):.1f}s]")

    
    sys.stdout.write(f"Zapisywanie zdjęcia '{final_image}': ")
    sys.stdout.flush()

    begin = time.time()
    new_image.save(final_image, format="PNG", compress_level=1)
    end = time.time()
    print(f"100% [{(end-begin):.1f}s]")

def find_suitable_images_for_pixels_in_rows(pixels, images_directory, row, pipe):
    images = []
    for pixel in pixels:
        r,g,b = pixel
        with open("rgb.txt", "r") as file:
            d_min = 196_000   # > (255^2) * 3
            for line in file:
                img_name,_r,_g,_b = line.split(";")
                _r = int(_r)
                _g = int(_g)
                _b = int(_b)

                d = (r-_r)**2 + (g-_g)**2 + (b-_b)**2

                if (d<d_min):
                    img_path = os.path.join(images_directory, img_name)
                    d_min = d
        images.append(img_path)

    pipe.send((images,row))



def main():
    images_directory = "seg_pred"
    image_to_mozaic = "fotka04.png"
    final_image = "final_img.png"

    tSize_mozaic = 4
    tSize_images = 16

    begin = time.time()
    calc_avg_rgb_for_images(images_directory, tSize_images)

    tiles_pixels = main_image_to_tiles(image_to_mozaic, tSize_mozaic)

    join_images(tiles_pixels, images_directory, final_image, tSize_images)

    end = time.time()
    print(f"\nŁączny czas operacji: {(end - begin)} s")

if __name__ == "__main__":
    main()