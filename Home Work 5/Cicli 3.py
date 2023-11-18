a = int(input("Введите А: "))
b = int(input("Введите В: "))
c = int(input("Введите С: "))
d = int(input("Введите D: "))
for i in range(c, d + 1):
    print(i, end="\t")
for i in range(a, b + 1):
    print("\n" + str(i), end="\t")
    for j in range(c, d + 1):
        print(i * j, end='\t')