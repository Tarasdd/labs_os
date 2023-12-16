cd /etc || exit 

file_count=$(find . -maxdepth 1 -type d ! -name '.*' | wc -l)

echo "count files: $file_count"
