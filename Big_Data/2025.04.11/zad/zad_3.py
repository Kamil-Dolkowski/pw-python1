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


def get_all_files_in_directory(directory):
    files = []

    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)

        if not os.path.isdir(file_path):
            files.append(file)

    return files

def average_RGB_from_image(img_name, img_directory):
    img_path = os.path.join(img_directory, img_name)

    img = Image.open(img_path)
    pixels = img.load()
    cols, rows = img.size

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

def calc_avg_rgb_for_images(images_directory):
    with open("rgb.txt", "w") as file:
        file.write("")

    images = get_all_files_in_directory(images_directory)
    workers = []

    for image in images:
        worker = multiprocessing.Process(target=average_RGB_from_image, args=(image, images_directory))
        workers.append(worker)
        worker.start()

    for worker in workers:
        worker.join()

def main_image_to_tiles(img_name, tSize):
    img = Image.open(img_name)
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

def join_images(tiles_pixels, images_directory, tSize = 150):
    workers = []
    pipes = []
    rows,cols = len(tiles_pixels[0]) * tSize, len(tiles_pixels[0]) * tSize

    new_image = Image.new("RGB", (rows, cols))
    new_pixels = new_image.load()

    for i in range(int(cols/tSize)):
        for j in range(int(rows/tSize)):
            pipeParent, pipeChild = Pipe()

            worker = multiprocessing.Process(
                target = find_suitable_image_for_pixel, 
                args = (
                    tiles_pixels[i][j], 
                    images_directory,  
                    i, j, 
                    pipeChild
                )
            )
            workers.append(worker)
            pipes.append(pipeParent)
            worker.start()

    
    for worker in workers:
        worker.join()

    for p in pipes:
        img_path,i,j = p.recv()

        image = Image.open(img_path)
        pixels = image.load()

        for x in range(tSize):
            for y in range(tSize):
                new_pixels[i*tSize+x, j*tSize+y] = pixels[x, y]
                
    new_image.save(f"final_img.png")

def find_suitable_image_for_pixel(pixel, images_directory, i, j, pipe):
    r,g,b = pixel
    with open("rgb.txt", "r") as file:
        d_min = 17_000_000
        for line in file:
            img_name,_r,_g,_b = line.split(";")
            _r = int(_r)
            _g = int(_g)
            _b = int(_b)

            d = (r-_r)**2 + (g-_g)**2 + (b-_b)**2

            if (d<d_min):
                img_path = os.path.join(images_directory, img_name)
                d_min = d

    pipe.send((img_path,i,j))



def main():
    images_directory = "seg_pred"

    # begin = time.time()
    # calc_avg_rgb_for_images(images_directory)
    # end = time.time()
    # print(f"Calculate avg RGB: {end - begin} s")

    tiles_pixels = main_image_to_tiles("fotka04.png", 32)

    begin = time.time()
    join_images(tiles_pixels, images_directory, tSize = 150)
    end = time.time()
    print(f"Creating image: {end - begin} s")

if __name__ == "__main__":
    main()