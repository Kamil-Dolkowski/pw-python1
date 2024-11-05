#!/bin/bash

mkdir ZADANIE3

echo "Podaj 5-literową nazwę pliku (małe litery): "
read nazwa_pliku

if [ ${#nazwa_pliku} = 5 ]; then
    touch ZADANIE3/${nazwa_pliku}

    data=`date`

    echo ${data} >> ZADANIE3/${nazwa_pliku}

    echo "wrzesień 1956 roku (kalendarz)" >> ZADANIE3/${nazwa_pliku}

    cal 9 1956 >> ZADANIE3/${nazwa_pliku}

    echo ${data} >> ZADANIE3/${nazwa_pliku}
fi

cd ..