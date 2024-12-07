#!/bin/bash

5_tests() {
    result_c=0
    result_d=0

    case "$compress_type" in
        ("gzip") 
            compress="gzip_compress"
            decompress="gzip_decompress"
            compress_file_extension="gz"
            ;;
        ("bzip2")
            compress="bzip2_compress"
            decompress="bzip2_decompress"
            compress_file_extension="bz2"
            ;;
        ("xz")
            compress="xz_compress"
            decompress="xz_decompress"
            compress_file_extension="xz"
            ;;
        ("zstd")
            compress="zstd_compress"
            decompress="zstd_decompress"
            compress_file_extension="zst"
            ;;
        ("lz4")
            compress="lz4_compress"
            decompress="lz4_decompress"
            compress_file_extension="lz4"
            ;;
        ("7z")
            compress="7z_compress"
            decompress="7z_decompress"
            compress_file_extension="7z"
            ;;
    esac

    for i in {1..5} ; do
    # compress
    start=`date +%s.%N`
    $compress
    end=`date +%s.%N`

    time_c=$(echo "$end - $start" | bc -l)
    result_c=$(echo "$result_c+$time_c" | bc -l)


    # decompress
    start=`date +%s.%N`
    $decompress
    end=`date +%s.%N`
    
    time_d=$(echo "$end - $start" | bc -l)
    result_d=$(echo "$result_d+$time_d" | bc)
    done

    echo -en "$(echo "$result_c/5" | bc -l | awk '{printf "%.8f",$0}')\t"
    echo -en "$(echo "$result_d/5" | bc -l | awk '{printf "%.8f",$0}')\t"

    original_file=$(du $tmp_dir/archive.tar | awk '{print $1}')
    compress_file=$(du $tmp_dir/archive.tar.$compress_file_extension | awk '{print $1}')

    echo "100*$compress_file/$original_file" | bc -l | awk '{printf "%.1f",$0}' && echo "%"
}

gzip_compress() {
    yes n | gzip -k $tmp_dir/archive.tar 2> /dev/null
}

gzip_decompress() {
    yes n | gzip -d $tmp_dir/archive.tar.gz 2> /dev/null
}

bzip2_compress() {
    bzip2 -k $tmp_dir/archive.tar 2> /dev/null
}

bzip2_decompress() {
    bzip2 -d $tmp_dir/archive.tar.bz2 2> /dev/null
}

xz_compress() {
    xz -k $tmp_dir/archive.tar 2> /dev/null
}

xz_decompress() {
    xz -d $tmp_dir/archive.tar.xz 2> /dev/null
}

zstd_compress() {
    yes n | zstd $tmp_dir/archive.tar 2> /dev/null
}

zstd_decompress() {
    yes n | zstd -d $tmp_dir/archive.tar.zst 2> /dev/null
}

lz4_compress() {
    lz4 -c $tmp_dir/archive.tar > $tmp_dir/archive.tar.lz4 2> /dev/null
}

lz4_decompress() {
    lz4 -dk $tmp_dir/archive.tar.lz4 2> /dev/null
}

7z_compress() {
    yes n | 7z a $tmp_dir/archive.tar.7z $tmp_dir/archive.tar > /dev/null
}

7z_decompress() {
    yes n | 7z x $tmp_dir/archive.tar.7z > /dev/null
}




tmp_dir=$(mktemp -d)


for path in "$@" ; do
    tar cvf "$tmp_dir/archive.tar" $path > /dev/null 2> /dev/null

    echo -e "\n$path"
    echo -e "name\tcompress\tdecompress\tratio"

    echo -en "gzip\t"
    compress_type="gzip"
    5_tests
    
    echo -en "bzip2\t"
    compress_type="bzip2"
    5_tests

    echo -en "xz\t"
    compress_type="xz"
    5_tests
    
    echo -en "zstd\t"
    compress_type="zstd"
    5_tests

    echo -en "lz4\t"
    compress_type="lz4"
    5_tests

    echo -en "7z\t"
    compress_type="7z"
    5_tests

    rm $tmp_dir/*
done


rm -rf $tmp_dir