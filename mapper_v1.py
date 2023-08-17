import sys

for file_line in sys.stdin:
    words = file_line.strip().split()

    for word in words:
        print(f"{word}\t1")