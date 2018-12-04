two = 0
three = 0

with open('input.txt', 'r') as f:
    for line in f.readlines():
        for letter in list(set(line)):
            if line.count(letter) == 2:
                two += 1
                break
        for letter in list(set(line)):
            if line.count(letter) == 3:
                three += 1

print(str(two*three))
