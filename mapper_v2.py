import sys
import re

for file_line in sys.stdin:
    words = file_line.strip().split()

    for word in words:
        if re.fullmatch(r"[A-Za-z]+", word):
            print(f"{word}\t1")