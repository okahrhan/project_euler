#!/bin/bash
dir_name=$(echo "$1" | tr ' ' '_')
mkdir -p "$dir_name"
touch "$dir_name/${dir_name}.py"
echo "Created directory '$dir_name' and file '${dir_name}.py'"

