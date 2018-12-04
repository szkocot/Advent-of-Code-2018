from collections import Counter
from difflib import SequenceMatcher

data = [x for x in open('input.txt').readlines()]

length = len(data[0])
ratio = (length-1)/length


for i, name in enumerate(data):
    s = SequenceMatcher(a=name, b=data[i])

    for name2 in data[i+1:]:
        s.set_seq2(name2)
        if s.ratio() == ratio:
            result = ""
            for n1, n2 in zip(name, name2):
                if n1 == n2:
                    result += n1
            print(result)
