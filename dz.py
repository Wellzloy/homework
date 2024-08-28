n = int(input('Введите число от 3 до 20 '))
m = 0
number_ = []
while m < n:
    number_.append(m+1)
    m += 1
print(*number_)
print(number_)
number_key =[]
for i in number_:
    print('__________')
    print(i)
    print('__________')
    for j in range(i, n):
        print(f'i+j{i}+{j}={i+j}')
        k = n%(i+j)
        if k == 0:
            print('нашло')
            number_key.append(i)
            number_key.append(j)
            continue


print(number_key)


