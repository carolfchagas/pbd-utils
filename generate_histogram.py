import sys

def generate_histogram(frequencies):
    histogram = [0] * 10
    for freq in frequencies:
        index = min(9, freq // 50)
        histogram[index] += 1
    return histogram

file_name = sys.argv[1]

word_freq = []
with open(file_name, 'r') as file:
    for line in file:
        _, freq = line.strip().split()
        word_freq.append(int(freq))

histogram = generate_histogram(word_freq)

for i, count in enumerate(histogram):
    interval_start = i * 50
    interval_end = (i + 1) * 50 - 1
    if i == 9:
        interval_end = "mais"
    print(f"{interval_start}-{interval_end}: {count}")

