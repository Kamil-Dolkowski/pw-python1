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
    begin = time.time()
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

    end = time.time()
    print(f"Liczenie średnich RGB: 100% [{(end-begin):.1f}s]")

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

    print("Szukanie odpowiednich zdjęć:", end=" ")
    begin = time.time()

    for c in range(int(cols/tSize)):
        pipeParent, pipeChild = Pipe()

        worker = multiprocessing.Process(
            target = find_suitable_images_for_pixels_in_column, 
            args = (tiles_pixels[c], images_directory, c, pipeChild)
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

    number_of_cols = len(pipes)
    col_number = 1

    for p in pipes:
        images_paths,c = p.recv()

        r = 0
        for img_path in images_paths:
            
            image = Image.open(img_path)

            new_image.paste(image,(c*tSize,r*tSize))

            r+=1
        sys.stdout.write(f'\rŁączenie zdjęć: {int(100 * col_number/number_of_cols)}%')
        sys.stdout.flush()
        col_number += 1
    
    end = time.time()
    print(f" [{(end-begin):.1f}s]")


    print("Zapisywanie zdjęcia 'final_img.png':", end=" ")
    begin = time.time()
    new_image.save(f"final_img.png", format="PNG", compress_level=0)
    end = time.time()
    print(f"100% [{(end-begin):.1f}s]")

def find_suitable_images_for_pixels_in_column(pixels, images_directory, c, pipe):
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

    pipe.send((images,c))



def main():
    images_directory = "seg_pred"

    begin = time.time()
    calc_avg_rgb_for_images(images_directory)

    tiles_pixels = main_image_to_tiles("fotka04.png", 8)

    join_images(tiles_pixels, images_directory, tSize = 150)
    end = time.time()
    print(f"\nŁączny czas operacji: {(end - begin)} s")

if __name__ == "__main__":
    main()