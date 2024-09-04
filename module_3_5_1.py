number = 40203 # type int
str_number = str(number) # type str
fist = int(str_number[0]) # 4 type int
print(type(len(str_number)))
# while len(str_number) > 1: # Условие длинна str_number больше единцы
#     str_number = int(str_number[1:]) # делает срез и отсекает 0 в начале при переводе из str в int,
#     print(str_number)
for i in len(str_number):
    print(i)



