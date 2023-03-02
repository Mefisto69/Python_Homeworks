# Задача 16: 
# Требуется вычислить, сколько раз встречается некоторое число X 
# в массиве A[1..N]. Пользователь в первой строке вводит 
# натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X

# *Пример:*
# 5
# 1 2 3 4 5
# 3
# -> 1
from random import sample
import os
def clear(): return os.system('cls')
clear()

def get_count (user_lenth,user_number):
    new_list = sample(range(1,user_lenth+10), k=user_lenth)
    print(new_list)
    print(new_list.count(user_number))

get_count(int(input("Enter the number of items - ")),int(input("Enter the desired number - ")))