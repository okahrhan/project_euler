#!/bin/bash

# İlk parametreyi al ve boşlukları alt tire ile değiştir
dir_name=$(echo "$1" | tr ' ' '_')

# Dizin oluştur
mkdir -p "$dir_name"

# Python dosyasını oluştur
touch "$dir_name/${dir_name}.py"

echo "Created directory '$dir_name' and file '${dir_name}.py'"

