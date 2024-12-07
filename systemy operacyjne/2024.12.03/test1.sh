#!/bin/bash

measure_time() {
    local program=$1
    local file=$2
    local operation=$3
    local time_sum=0

    for i in {1..5}; do
        start=$(date +%s.%N)
        if [ "$operation" == "compress" ]; then
            case $program in
                gzip) gzip -c "$file" > "${file}.gz"; compressed_file="${file}.gz" ;;
                bzip2) bzip2 -c "$file" > "${file}.bz2"; compressed_file="${file}.bz2" ;;
                xz) xz -c "$file" > "${file}.xz"; compressed_file="${file}.xz" ;;
                zstd) zstd -c "$file" > "${file}.zst"; compressed_file="${file}.zst" ;;
                lz4) lz4 -c "$file" > "${file}.lz4"; compressed_file="${file}.lz4" ;;
                7z) 7z a -t7z -mx=9 "${file}.7z" "$file" > /dev/null; compressed_file="${file}.7z" ;;
            esac
        elif [ "$operation" == "decompress" ]; then
            case $program in
                gzip) gzip -dc "${file}" > /dev/null ;;
                bzip2) bzip2 -dc "${file}" > /dev/null ;;
                xz) xz -dc "${file}" > /dev/null ;;
                zstd) zstd -dc "${file}" > /dev/null ;;
                lz4) lz4 -dc "${file}" > /dev/null ;;
                7z) 7z x -y "${file}" -o"$tmp_dir/extracted" > /dev/null ;;
            esac
        fi
        end=$(date +%s.%N)
        elapsed=$(echo "$end - $start" | bc -l)
        time_sum=$(echo "$time_sum + $elapsed" | bc -l)
    done

    LC_NUMERIC=C printf "%.6f\n" "$(echo "$time_sum / 5" | bc -l)"
}

if [ "$#" -lt 1 ]; then
    echo "Usage: $0 directory1 [directory2 ...]"
    exit 1
fi

tmp_dir=$(mktemp -d)

for dir in "$@"; do
    echo -e "\nProcessing directory: $dir"
    tar_file="$tmp_dir/archive.tar"
    tar cvf "$tar_file" -C "$dir" . > /dev/null
    original_size=$(stat -c%s "$tar_file")
    echo -e "name\tcompress\tdecompress\tratio"

    programs=("gzip" "bzip2" "xz" "zstd" "lz4" "7z")
    for program in "${programs[@]}"; do
    compress_time=$(measure_time "$program" "$tar_file" "compress")
        
    case $program in
        gzip) compressed_file="${tar_file}.gz" ;;
        bzip2) compressed_file="${tar_file}.bz2" ;;
        xz) compressed_file="${tar_file}.xz" ;;
        zstd) compressed_file="${tar_file}.zst" ;;
        lz4) compressed_file="${tar_file}.lz4" ;;
        7z) compressed_file="${tar_file}.7z" ;;
    esac

    if [ ! -f "$compressed_file" ]; then
        echo -e "$program\tERROR\tERROR\tERROR"
        continue
    fi

    compressed_size=$(stat -c%s "$compressed_file")
    decompress_time=$(measure_time "$program" "$compressed_file" "decompress")
    ratio=$(echo "scale=2; $compressed_size / $original_size * 100" | bc -l)

    echo -e "$program\t$compress_time\t$decompress_time\t$ratio%"
    rm -f "$compressed_file"
done
    rm -f "$tar_file"
done

rm -rf "$tmp_dir"