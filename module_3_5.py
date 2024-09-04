def get_multiplied_digits(number):  # number тип int
    print(number, type(number))  # проверка number тип int
    str_number = str(number)  # str_number присваиваем number тип str
    print(str_number, type(str_number))  # проверка str_number тип str
    first = int(str_number[0])  # first присваиваем первый символ str_number переводим в тип int
    print(first, type(first))  # проверка first типа int
    print(len(str_number), 'Длинна str_number')  # длинна str_number
    if len(str_number) > 1:  # Если длинна str_number больше 1
        well_ = str_number[1:]  #
        print(well_, type(well_))  #
        print(int(well_), type(well_))  #
        first * get_multiplied_digits(well_)
    else:
        return first

        print('Stop')


get_multiplied_digits(40203)
