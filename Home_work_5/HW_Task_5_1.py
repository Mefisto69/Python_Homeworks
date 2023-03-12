# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; 
# B = 5 -> 243 (3⁵)
# A = 2; 
# B = 3 -> 8 

import os
def clear(): return os.system('cls')
clear()

def stepen(a,b):
    if b>0:
        return  a*stepen(a,b-1)
    return 1

a = int(input('A = '))
b = int(input('B = '))
print(f'{a} в степени {b} = {stepen(a,b)}')