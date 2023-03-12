# Задача 28: Напишите рекурсивную функцию sum(a, b), 
# возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.

# *Пример:*
# 2 2
#     4 

import os
def clear(): return os.system('cls')
clear()

def summa(a,b):
    if b>0:
        return summa(a+1,b-1)
    return a

a = int(input('A = '))
b = int(input('B = '))
print(f'{a} + {b} = {summa(a,b)}')