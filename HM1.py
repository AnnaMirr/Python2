import colorama
from colorama import Fore

colorama.init()

def input_num(x):
    check = True
    while check:
        try:
            number = int(input(x))
            if number >= 0:
                check = False
                return number
            else:
                print(Fore.RED + "\nНеверный ввод!\n" + Fore.RESET)
                continue
        except ValueError:
            print(Fore.RED + "\nНеверный ввод! Введите число.\n" + Fore.RESET)


def grossZero(promt):
    x = 0
    while not x > 0:
        x = input_num(promt)
        if x == 0:
            print(Fore.YELLOW + "\nЧисло должно быть больше нуля!\n" + Fore.RESET)
        return x

def triangle():
    a = b = c = 0
    while not a > 0:
        a = grossZero('Введите первую сторону: ')
    while not b > 0:
        b = grossZero('Введите вторую сторону: ')
    while not c > 0:
        c = grossZero('Введите третью сторону: ')

    def checkTriangle(a, b, c):
        if (c ** 2 == a ** 2 + b ** 2) or (a ** 2 == b ** 2 + c ** 2) or (b ** 2 == a ** 2 + c ** 2):
            return (Fore.YELLOW + "прямоугольный.\n")
        elif (c ** 2 < a ** 2 + b ** 2) or (a ** 2 < b ** 2 + c ** 2) or (b ** 2 < a ** 2 + c ** 2):
            return (Fore.YELLOW + "остроугольный.\n")
        elif (c ** 2 > a ** 2 + b ** 2) or (a ** 2 > b ** 2 + c ** 2) or (b ** 2 > a ** 2 + c ** 2):
            return (Fore.YELLOW + "тупоугольный.\n")

    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            print(Fore.YELLOW + "\nТреугольник равносторонний." + Fore.RESET)
        elif a == b or a == c or b == c:
            print(Fore.YELLOW + "\nТреугольник равнобедренный, ", checkTriangle(a, b, c) + Fore.RESET)
        else:
            print(Fore.YELLOW + "\nТреугольник ", checkTriangle(a, b, c) + Fore.RESET)
    else:
        print(Fore.YELLOW + "\nТреугольник не существует.\n" + Fore.RESET)