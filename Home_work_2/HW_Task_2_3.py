# Задача 14
# Требуется вывести все целые степени двойки 
# (т.е. числа вида 2k), не превосходящие числа N.

import os
clear = lambda: os.system('cls')
clear()

number_n = int(input('Enter N: '))
i = 0
while 2 ** i <= number_n:
    print(2 ** i)
    i += 1