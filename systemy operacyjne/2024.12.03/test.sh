#!/bin/bash

tmp_dir=$(mktemp -d)

for path in "$@" ; do
    tar cvf "$tmp_dir/archive.tar" $path > /dev/null

    lz4 -c $tmp_dir/archive.tar > $tmp_dir/archive.tar.lz4 
    echo "$?"

    ls "$tmp_dir"
done

rm -rf $tmp_dir