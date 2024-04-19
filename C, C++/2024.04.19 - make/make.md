# Make

#-----------------------------------------------------------------------------------------

$ touch makefile


target: wymagania
    command1        (przed musi być tabulacja!, nie spacje!)
    command2

#-------------------------------------------

say:
        echo "Hello world"

#- - - - - - - - - - - - 

$ make
echo "Hello world"
Hello world

#-------------------------------------------

say:
        echo "Hello world"
say2:
        echo "Hello world2"

#- - - - - - - - - - - - 

$ make
echo "Hello world"
Hello world

$ make say2
echo "Hello world2"
Hello world2

#---------------------@---------------------

say:
        @echo "Hello world"     (@ - nie wyświetli polecenia, ale wyświetli jego efekt)
say2:
        echo "Hello world2"

#- - - - - - - - - - - - 

$ make
Hello world

$ make say2
echo "Hello world2"
Hello world2

#----------------SUB_TARGET-----------------

say:
        @echo "Hello world"

say2:
        echo "Hello world2"

target: sub_target
        echo "Target"

sub_target:
        echo "sub_target"

#- - - - - - - - - - - - 

$ make target
echo "sub_target"
sub_target
echo "Target"
Target

#--------------SUB_TARGET (PLIK)--------------

say:
        @echo "Hello world"

say2:
        echo "Hello world2"

target: sub_target
        echo "Target"

sub_target:
        echo "sub_target"

#- - - - - - - - - - - -

$ touch sub_target

$ ls -la
-rw-r--r-- 1 u04 u04  121 04-19 10:04 makefile
-rw-r--r-- 1 u04 u04    0 04-19 10:13 sub_target

$ make target
echo "Target"
Target

#------------------PHONY--------------------

.PHONY: sub_target              (nie szuka pliku sub_target)

say:
        @echo "Hello world"

say2:
        echo "Hello world2"

target: sub_target
        echo "Target"

sub_target:                     (nie jest traktowany jako plik)
        echo "sub_target"

#- - - - - - - - - - - -

$ ls -la
-rw-r--r-- 1 u04 u04  121 04-19 10:04 makefile
-rw-r--r-- 1 u04 u04    0 04-19 10:13 sub_target

$ make target
echo "sub_target"
sub_target
echo "Target"
Target

#----------------DEFAULT_GOAL----------------

.PHONY: sub_target
.DEFAULT_GOAL := say2

say:
        @echo "Hello world"

say2:
        echo "Hello world2"

target: sub_target
        echo "Target"

sub_target:
        echo "sub_target"

#- - - - - - - - - - - -

$ make
echo "Hello world2"
Hello world2

#--------------------ALL---------------------

.PHONY: sub_target
.DEFAULT_GOAL := say2

all: say say2                       (taki 'main')

say:
        @echo "Hello world"

say2:
        echo "Hello world2"

target: sub_target
        echo "Target"

sub_target:
        echo "sub_target"

#- - - - - - - - - - - -

$ make all
Hello world
echo "Hello world2"
Hello world2

#-------------------------------------------  (nie zadziałało na raspberry)

.PHONY: sub_target
.DEFAULT_GOAL := say2

all: say say2

say:
        @echo "Hello world"

say2:
        echo "Hello world2"

target: sub_target
        echo "Target"

sub_target:
        echo "sub_target"

generate:
        touch file{1..10}.txt

#- - - - - - - - - - - -



#-------------------------------------------

.PHONY: sub_target
.DEFAULT_GOAL := say2

all: say say2

say:
        @echo "Hello world"

say2:
        echo "Hello world2"

target: sub_target
        echo "Target"

sub_target:
        echo "sub_target"

generate:
        touch file{1..10}.txt

clean:
        rm *.txt

#- - - - - - - - - - - -

$ make clean
usunie wszystkie pliki .txt

#-------------------------------------------------------------------------------------------------------------------------------------------------------

#-------------------------------------------

file := file_1 file_2

file_main: $(file)
        @echo "file_main"
        @echo "Variable: " $(file)
        @touch file_main

file_1:
        @echo "file_1"
        @touch file_1.txt

file_2:
        @echo "file_2"
        @touch file_2.txt

#- - - - - - - - - - - -

$ make
file_1
file_2
file_main
Variable:  file_1 file_2

$ ls -la
-rw-r--r-- 1 u04 u04    0 04-19 10:45 file_1.txt
-rw-r--r-- 1 u04 u04    0 04-19 10:45 file_2.txt
-rw-r--r-- 1 u04 u04    0 04-19 10:45 file_main
-rw-r--r-- 1 u04 u04  195 04-19 10:44 makefile

#-------------------------------------------------------------------------------------------------------------------------------------------------------

#-------------------------------------------

target: 
        echo $@         ($@ - target)
        echo $<         ($< - pierwszy element)

#- - - - - - - - - - - -

$ make
echo target
target
echo
                (puste)

#-------------------------------------------

target: cond_1 cond_2
        echo $@
        echo $<

cond_1:
        @echo "c1"

cond_2:
        @echo "c2"

#- - - - - - - - - - - -

$ make
c1
c2
echo target
target
echo cond_1
cond_1

#-------------------------------------------

target: cond_1 cond_2
        echo $@
        echo $<
        echo $^         ($^ - wszystkie elementy)

cond_1:
        @echo "c1"

cond_2:
        @echo "c2"

#- - - - - - - - - - - -

$ make
c1
c2
echo target
target
echo cond_1
cond_1
echo cond_1 cond_2
cond_1 cond_2

#-------------------------------------------

target: cond_1 cond_2
        echo $@
        echo $<
        echo $^

cond_1:
        @echo "c1"
        touch c1.txt

cond_2:
        @echo "c2"
        touch c2.txt

files_txt := $(wildcard *.txt)          (wildcard - szuka wzorca)

cond_3: $(files_txt)
        @echo "All txt files"
        @echo $^

#- - - - - - - - - - - -

$ ls -la
-rw-r--r-- 1 u04 u04    0 04-19 11:02 c1.txt
-rw-r--r-- 1 u04 u04    0 04-19 11:02 c2.txt
-rw-r--r-- 1 u04 u04  207 04-19 11:01 makefile

$ make cond_3
All txt files
c1.txt c2.txt

#-------------------------------------------  (problemy na raspberry)

target: cond_1 cond_2
        echo $@
        echo $<
        echo $^
        @echo "Updated:"
        echo $?         ($? - nowsze cele, mają znacznik czasowy ?? niż target)
        touch target

cond_1:
        @echo "c1"
        touch c1.txt

cond_2:
        @echo "c2"
        touch c2.txt

files_txt := $(wildcard *.txt)

cond_3: $(files_txt)
        @echo "All txt files"
        @echo $^

#- - - - - - - - - - - -

$ touch target

$ make
target nie powinien się utworzyć

#-------------------------------------------------------------------------------------------------------------------------------------------------------

#-----------------MAIN.C-------------------

#include <stdio.h>
#include <stdlib.h>

#include "external.h"

int main() {
    bar();
    return EXIT_SUCCESS;
}

#----------------EXTERNAL.C-----------------

#include <stdio.h>

void bar() {
    printf("Hello bar\n");
}

#----------------EXTERNAL.H-----------------

#ifndef EXTERNAL_H
#define EXTERNAL_H

void bar();

#endif

#----------------MAKEFILE 1------------------ 

main: main.c external.c
        gcc main.c external.c -o main

#- - - - - - - - - - - -

$ make
gcc main.c external.c -o main

$ ls -la
-rw-r--r-- 1 u04 u04    62 04-19 11:58 external.c
-rw-r--r-- 1 u04 u04    59 04-19 11:56 external.h
-rwxr-xr-x 1 u04 u04 70544 04-19 12:02 main
-rw-r--r-- 1 u04 u04   114 04-19 11:53 main.c
-rw-r--r-- 1 u04 u04    55 04-19 12:02 makefile

$ ./main
Hello bar

#----------------MAKEFILE 2------------------ (file.c -> file.o) [wbudowane w make]

main: main.o external.o
        gcc main.o external.o -o main

#- - - - - - - - - - - -

$ ls -la
-rw-r--r-- 1 u04 u04    62 04-19 11:58 external.c
-rw-r--r-- 1 u04 u04    59 04-19 11:56 external.h
-rwxr-xr-x 1 u04 u04 70544 04-19 12:02 main
-rw-r--r-- 1 u04 u04   114 04-19 11:53 main.c
-rw-r--r-- 1 u04 u04    55 04-19 12:02 makefile

$ make
cc    -c -o main.o main.c
cc    -c -o external.o external.c
gcc main.o external.o -o main

$ ls -la
-rw-r--r-- 1 u04 u04    62 04-19 11:58 external.c
-rw-r--r-- 1 u04 u04    59 04-19 11:56 external.h
-rw-r--r-- 1 u04 u04  1600 04-19 12:05 external.o
-rwxr-xr-x 1 u04 u04 70544 04-19 12:07 main
-rw-r--r-- 1 u04 u04   114 04-19 11:53 main.c
-rw-r--r-- 1 u04 u04  1400 04-19 12:07 main.o
-rw-r--r-- 1 u04 u04    55 04-19 12:07 makefile

#-------------------------------------------

%.o: %.c

main.o: main.c
external.o: external.c

#----------------MAKEFILE 2------------------ (file.c -> file.o) [własnoręcznie zrobione]

main: main.o external.o
        gcc main.o external.o -o main

%.o: %.c
        @echo $<
        @echo $@
        gcc -c $< -o $@

clean:
        rm *.o

#- - - - - - - - - - - -

$ make clean
rm *.o

$ make
main.c
main.o
gcc -c main.c -o main.o
external.c
external.o
gcc -c external.c -o external.o
gcc main.o external.o -o main

#----------------MAKEFILE 3------------------ (wrzucenie plików .o do wspólnego katalogu obj)

DIROBJ := obj

_OBJ = main.o external.o
OBJ = $(patsubst %, $(DIROBJ)/%, $(_OBJ))

t:
        echo $(OBJ)

main: $(OBJ)
        gcc $^ -o $@

%.o: %.c
        @echo $<
        @echo $@
        gcc -c $< -o $@

clean:
        rm *.o

#- - - - - - - - - - - -

$ make
echo  obj/main.o  obj/external.o
obj/main.o obj/external.o

#-------------------------------------------

OBJ = $(patsubst %, $(DIROBJ)/%, $(_OBJ))        -> 'for each'

$(_OBJ) -> %
tworzy ścieżkę -> $(DIROBJ)/%

#----------------MAKEFILE 3------------------

DIROBJ := obj

_OBJ = main.o external.o
OBJ = $(patsubst %, $(DIROBJ)/%, $(_OBJ))

t:
        echo $(OBJ)

main: $(OBJ)
        gcc $^ -o $@

$(DIROBJ)/%.o: %.c
        @echo $<
        @echo $@
        gcc -c $< -o $@

clean:
        rm *.o

#- - - - - - - - - - - -

$ mkdir obj

$ make main
main.c
obj/main.o
gcc -c main.c -o obj/main.o
external.c
obj/external.o
gcc -c external.c -o obj/external.o
gcc obj/main.o obj/external.o -o main

$ ls -la
-rw-r--r-- 1 u04 u04    62 04-19 11:58 external.c
-rw-r--r-- 1 u04 u04    59 04-19 11:56 external.h
-rwxr-xr-x 1 u04 u04 70544 04-19 12:46 main
-rw-r--r-- 1 u04 u04   114 04-19 11:53 main.c
-rw-r--r-- 1 u04 u04   201 04-19 12:45 makefile
drwxr-xr-x 2 u04 u04  4096 04-19 12:46 obj

$ ls -l obj/
-rw-r--r-- 1 u04 u04 1600 04-19 12:46 external.o
-rw-r--r-- 1 u04 u04 1400 04-19 12:46 main.o

#----------------MAKEFILE 3------------------ (poprawki)

DIROBJ := obj

_OBJ = main.o external.o
OBJ = $(patsubst %, $(DIROBJ)/%, $(_OBJ))

all: main

main: $(OBJ)
        gcc $^ -o $@

$(DIROBJ)/%.o: %.c
        @echo $<
        @echo $@
        gcc -c $< -o $@

.PHONY: clean

clean:
        rm $(DIROBJ)/*.o

#-------------------------------------------
