#!/bin/bash

output="index.html"

echo "<html>" > $output
echo "<head><title>Game Index</title><style>button { border: 2px solid #141414; border-radius: 10px; padding: 10px 20px; margin: 5px; background: white; cursor: pointer; font-family: Arial, sans-serif; }</style></head>" >> $output
echo "<body><h1>Games</h1><div>" >> $output

find . -name "*.html" -type f | sort | while read file; do
    name=$(basename "$file" .html)
    name=${name:2}
    echo "<a href=\"$file\"><button>$name</button></a>" >> $output
done

echo "</div></body></html>" >> $output