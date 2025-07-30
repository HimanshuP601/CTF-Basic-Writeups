#!/bin/bash

# Loop through files starting with numbers from 10 to 20
for file in [1-2][0-9]*.md; do
    # Extract current number prefix
    old_num=$(echo "$file" | cut -d'.' -f1)

    # Only rename if number is between 10 and 20
    if [ "$old_num" -ge 10 ] && [ "$old_num" -le 20 ]; then
        # Calculate new number
        new_num=$((old_num + 6))

        # Get rest of the filename (remove the number and dot)
        rest=$(echo "$file" | cut -d'.' -f2-)

        # Rename file
        mv "$file" "${new_num}.${rest}"
    fi
done
