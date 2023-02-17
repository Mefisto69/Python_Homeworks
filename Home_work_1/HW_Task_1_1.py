# Задача 2: Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)

import os
def clear(): return os.system('cls')

clear()
User_number = int(input("Enter a three-digit number: "))
Resultvalue = 0
if User_number<1000 and User_number>0:
    Resultvalue = (User_number//100) + ((User_number%100)//10)+ (User_number%10)
    print(f'sum of three digits of "{User_number}" = {Resultvalue}')
else:
    print("ERROR! Enter a three-digit number!")
