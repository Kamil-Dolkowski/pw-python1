#!/bin/bash

gzip_compress() {
    start=`date +%s.%N`
    gzip -k $tmp_dir/archive.tar 
    end=`date +%s.%N`

    result=$(echo "$end - $start" | bc -l)
    
    echo -en "$result\t"
}

gzip_decompress() {
    start=`date +%s.%N`
    gzip -d $tmp_dir/archive.tar.gz
    end=`date +%s.%N`

    result=$(echo "$end - $start" | bc -l)

    echo -en "$result\t"
}

decompress() {
    pass
}





tmp_dir=$(mktemp -d)


for path in "$@" ; do
    tar cvf "$tmp_dir/archive.tar" $path

    echo "$path"
    echo -e "name\t compress\t decompress\t ratio"

    echo -en "gzip\t"
    gzip_compress
    gzip_decompress
    
    rm $tmp_dir/archive.tar
done


ls $tmp_dir

# tar cvf $temp/random.tar $path_random
#tar cvf $temp/empty.tar $path_empty
#tar cvf $temp/various.tar $path_various

# tar cvf random.tar /tmp/data/random
# gzip -k random.tar

rm -rf $tmp_dir

# bc ?