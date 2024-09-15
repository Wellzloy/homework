class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        print(f'Номер нового этажа {new_floor}')

# h1 = House('ЖК Горский', 18)
# Метод go_to выводит на экран(в консоль) значения от 1 до new_floor(включительно).
# Если же new_floor больше чем self.number_of_floors или меньше 1, то вывести строку "Такого этажа не существует".

well_ = House('Сосенки', 5)
print(well_.name, well_.number_of_floors)