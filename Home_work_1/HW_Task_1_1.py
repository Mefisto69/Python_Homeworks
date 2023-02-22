# Задача 2: Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)

import os
def clear(): return os.system('cls')

clear()
# User_number = int(input("Enter a three-digit number: "))
# Resultvalue = 0
# if User_number<1000 and User_number>0:
#     Resultvalue = (User_number//100) + ((User_number%100)//10)+ (User_number%10)
#     print(f'sum of three digits of "{User_number}" = {Resultvalue}')
# else:
#     print("ERROR! Enter a three-digit number!")

# ---------------Вариант 2 (Для любого количества цифр)

# User_number = int(input("Введите число: "))
# Resultvalue = 0
# while User_number > 0:
#     ostatok = User_number % 10
#     Resultvalue += ostatok
#     User_number//=10
# print(f'Сумма цифр данного числа = {Resultvalue}')

# Список -----------------------
User_number = input("Введите число: ")
Resultvalue = 0
if len(User_number) != 3:
    print("ERROR! Enter a three-digit number!")
else:
    Resultvalue = int (User_number[0])+ int (User_number[1])+int (User_number[2])
    print(f'Сумма цифр данного числа = {Resultvalue}')
