freq = 0

with open('input.txt', 'r') as f:
    for line in f.readlines():
        freq += int(line)

    print('Frequency = ', str(freq))
