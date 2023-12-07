from itertools import permutations

def slova(x):
    x = ''.join(sorted(x))
    words = set()
    for i in range(1, len(x) + 1):
        for j in permutations(x, i):
            word = ''.join(j)
            if word not in words:
                words.add(word)
                print(word)
    return len(words)

a = "Калиев"
count = slova(a)
print(count)
