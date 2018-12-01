freq = 0
saved_freqs = set()
not_found = True
times = 1
data = [int(x) for x in open('input.txt').readlines()]

while not_found:
    for line in data:
        freq += line
        if freq in saved_freqs:
            print('Frequency = ', str(freq))
            not_found = False
            break
        saved_freqs.add(freq)
    print('Tried ', str(times), ' times')
    times += 1
