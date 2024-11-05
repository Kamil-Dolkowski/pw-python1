#!/bin/bash
echo -n "Podaj liczbę naturalną (1-100): "
read liczba # wczytywanie z terminala do zmiennej liczba
echo -n "podałeś: "
echo $liczba
echo ${liczba} # inne odwołanie do zmiennej − dlaczego tak?
echo "Dziś jest ${liczba}dni od poczatku awarii systemu"
#echo "Dziś jest $liczbadni od początku awarii systemu" # tak nie zadziała
dzien=`date` # przypisanie do zmiennej wyniku polecenia systemowego
echo "Dzisiejsza data to: "
echo $dzien # odwołanie sie do zmiennej
# dostęp do zmiennych systemowych
echo "Twoj katalog domowy to: ${HOME}"
nazwa=QWERTY # zmienna nazwa przechowuje nazwę katalogu do utworzenia
mkdir $nazwa # tworzenie katalogu
cd $nazwa # wejście do katalogu
touch example.txt # stworzenie pliku w katalogu nazwa