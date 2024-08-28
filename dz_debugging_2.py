n = 11
number_ = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11]
number_key =[]
for i in number_:
    print('__________')
    print(i)
    print('__________')
    for j in range(i, n):
        print(f'i+j   {i}+{j}={i+j}')
        k = n%(i+j)
        if k == 0:
            print('нашло', i ,j)
            number_key.append(i)
            number_key.append(j)
            continue


print(number_key)




