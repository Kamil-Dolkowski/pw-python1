# https://fulmanski.pl/zajecia/big_data/zajecia_20212022/projects.php
# 3 zbiór (150 x 150 px)

# przeskalowanie katalogu
# średnie RGB dla każdego z obrazków
# zapis do pliku/bazy danych
# zamiana pikseli głównego obrazka na obrazki

import os
from PIL import Image



def get_all_files_in_directory(images_directory):
    files = []

    for file in os.listdir(images_directory):
        file_path = os.path.join(images_directory, file)

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
            
    return (r,g,b)



def main():
    images_directory = "Images"

    x = average_RGB_from_image("fotka05.png", images_directory)
    print(x)


if __name__ == "__main__":
    main()