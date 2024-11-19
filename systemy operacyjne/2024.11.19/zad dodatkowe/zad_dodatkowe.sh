#!/bin/bash

pierwsza=0
counter=0

while [ true ] ; do
    echo "Podaj liczbe: "
    read number

    
    if [ $(echo "$number" | grep -E "^-?[[:digit:]]+$") ]; then
        
        # liczba ujemna 
        if [ "$number" -lt 0 ]; then
            newNumber=$((-$number))
            echo $newNumber >> abs.txt
        # liczba dodatnia  
        elif [ "$number" -gt 0 ]; then
            if [ $number -ne 1 ]; then
                for i in $(seq 2 $(($number-1))); do
                    if [ $(($number%$i)) -eq 0 ]; then
                        pierwsza=1
                        break
                    fi
                done
                if [ $pierwsza -eq 0 ]; then
                    echo "$number" >> prime.txt
                    ((counter++))
                fi
                pierwsza=0
            fi
        # zero 
        elif [ "$number" -eq 0 ]; then
            #cat prime.txt | grep -E -c "^.+$" 
            echo "$counter"
            exit
        fi
    fi

done