#!/bin/bash

path1='tmp/data/empty'
path2='tmp/data/random'
path3='tmp/data/various'



dd if=/dev/zero of=$path1/empty1 bs=10M count=1
dd if=/dev/zero of=$path1/empty2 bs=10M count=1
dd if=/dev/zero of=$path1/empty3 bs=10M count=1
dd if=/dev/zero of=$path1/empty4 bs=10M count=1
dd if=/dev/zero of=$path1/empty5 bs=10M count=1


dd if=/dev/urandom of=$path2/random1 bs=10M count=1
dd if=/dev/urandom of=$path2/random2 bs=10M count=1
dd if=/dev/urandom of=$path2/random3 bs=10M count=1
dd if=/dev/urandom of=$path2/random4 bs=10M count=1
dd if=/dev/urandom of=$path2/random5 bs=10M count=1

# dd if=/dev/zero of=tmp/data/empty/empty5 bs=10M count=1