#!/bin/bash
# polecane

i=1
FILE="dane2.csv"
while IFS="," read -r imienazwisko szkola panpani
do
    echo "$i. $imienazwisko $szkola"
    i=$(($i+1))
done < $FILE