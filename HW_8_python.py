# ЗАДАНИЕ 1.
# Создать список из чисел и имен, а также перебрать список в цикле и
# отделить текст от чисел и вывести текст на экран и создать новый список состоящий только
# из текста, числа сложить с 10 и также вывести на экран и создать список состоящий только из чисел.


# Создать список из чисел и имен
list_Name_Age = [
    "Kirill", 10, "Semen", 20, "Igor", 18, "Klavdia", 16, "Ivan", 17,
    "Max", 30, "Irina", 7, "Konstantin", 25, "Olga", 14, "Pavel", 25
]

# print(list_Name_Age)
# print(list_Name_Age.sort)

listName = []
listAge = []

for x in list_Name_Age:
    if type(x) == str:
        listName.append(x)
    if type(x) == int:
        listAge.append(x)
print(listName)
print(listAge)
listAge.sort(reverse=True)  # Сортировка по убыванию
print(f'after sorting {listAge}')

with open("testHW_8.txt", "w") as file:  # записали и создали в файле
    file.write(str(listAge))
    file.write(str(listName))

for x in range(len(listAge)):
    # Функция len() используется для возврата количества элементов, а range() — списка индексов.
    listAge[x] += 10
with open("testHW_8.txt", "w") as file:  # записали и создали в файле
    file.write(str(listAge))

print(listAge)

# ЗАДАНИЕ 2.
# Создать словарь игрового персонажа который будет иметь следующие свойства: имя, кол-во жизней, кол-во маны,
# силу, ловкость, выносливость, физическую стойкость, магическую стойкость.
# Распечатать словарь по ключу применяя читаемый текст

game_character = \
    {
        "Имя": "Maksim", "Кол-во жизней": 5, "Кол-во маны": 100, "Сила": 100,
        "Ловкость": 50, "Выносливость": 50, "Физическая стойкость": 80, "Магическая стойкость": 90
    }
# print(game_character)


def main():
    for key, value in game_character.items():
        print(key, ':', value)


if __name__ == '__main__':
    main()

# ЗАДАНИЕ 3.
# Написать программу которая будет принимать на вход string и конвертировать str в int.
# Затем описать короткую программу вычисления двух чисел, при которой арифметический знак также
# должен вводиться с клавиатуры.

# pip install colorama - модуль цветов
from colorama import init
from colorama import Fore, Back, Style
init()
# ЦВЕТ ТЕКСТА: Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# ЦВЕТ ФОНА: Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.

what = str(input("ЧТО ДЕЛАЕМ? (+, -, *, /): "))

number_1 = str(input("Введите первое число: "))
number_2 = str(input("Введите первое число: "))

print(Fore.BLACK)
print(Back.YELLOW)
if what == "+":
    print("Результат : ",  + int(number_1) + int(number_2))
elif what == "-":
    print("Результат : ",  + int(number_1) - int(number_2))
elif what == "*":
    print("Результат : ",  + int(number_1) * int(number_2))
elif what == "/":
    print("Результат : ",  + int(number_1) / int(number_2))
else:
    print("Выбрана неверная операция")