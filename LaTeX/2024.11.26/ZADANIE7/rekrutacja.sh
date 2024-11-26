#!/bin/bash

pliktex="rekrutuj.tex"
plikpdf="rekrutuj.pdf"

dane="daneStudenci.csv"



touch $pliktex

echo "\documentclass[12pt,a4paper]{article}

\usepackage[margin=2cm]{geometry}
\usepackage[utf8]{inputenc}
\usepackage{polski}
\usepackage{enumerate}

\begin{document}" > $pliktex



while IFS=',' read -r lp katalog nazwisko imie wydzial wiek plec
do
    if [ $lp = "Lp." ] ; then
        continue
    fi

    echo "\hfill Płock, 19 listopada 2024 r.\\\\ " >> $pliktex
    echo "\noindent " >> $pliktex

    if [ $plec = "M" ] ; then
        echo "Szanowny Pan \\\\" >> $pliktex
    else 
        echo "Szanowna Pani \\\\" >> $pliktex
    fi

    echo "$imie $nazwisko \\\\" >> $pliktex
    echo "wiek: $wiek" >> $pliktex

    echo "" >> $pliktex
    echo "\bigskip" >> $pliktex
    echo "" >> $pliktex

    echo "\begin{center}" >> $pliktex
    echo "{\Large\textbf{Zawiadomienie}}" >> $pliktex
    echo "\end{center}" >> $pliktex

    echo "\bigskip" >> $pliktex

    if [ $plec = "M" ] ; then
        echo "Z radością chcielibyśmy poinformować Pana, że w wyniku procesu rekrutacyjnego" >> $pliktex
        echo "\begin{center}" >> $pliktex
        echo "\textsf{\textbf{został Pan przyjęty}} " >> $pliktex
    else
        echo "Z radością chcielibyśmy poinformować Panią, że w wyniku procesu rekrutacyjnego" >> $pliktex
        echo "\begin{center}" >> $pliktex
        echo "\textsf{\textbf{została Pani przyjęta}} " >> $pliktex
    fi

    echo "\end{center}" >> $pliktex
    echo "na Wydział Elektroniki z identyfikatorem \verb|$katalog|." >> $pliktex

    echo "\vspace{2cm}" >> $pliktex
    echo "" >> $pliktex
    echo "\noindent" >> $pliktex
    echo "Z poważaniem,\\\\" >> $pliktex
    echo "Dziekan" >> $pliktex
    echo "Wydziału Elektroniki" >> $pliktex

    echo "\newpage" >> $pliktex

done < $dane



echo "\end{document}" >> $pliktex




pdflatex $pliktex
pdflatex $pliktex

evince $plikpdf # otwiera plik pdf