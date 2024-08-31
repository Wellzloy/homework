n = int(input('Введите число от 3 до 20 '))
number_key = []
for i in range(1, n):
    for j in range(i + 1, n):
            if (n % (i + j)) == 0:
                number_key.append(i, j)
                number_key.append(j)
            continue
print(' '.join(map(str, number_key)))
