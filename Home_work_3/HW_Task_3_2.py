# Задача 18: 
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
# 1 2 3 4 5
# 6
# -> 5

from random import sample
import os
def clear(): return os.system('cls')
clear()

def get_list (user_lenth):
    get_items = sample((range(1, user_lenth+10)), k=user_lenth)
    return get_items

def nearest_element(items, user_number):  
    return min(items, key=lambda x: abs(user_number - abs(x)))

A = get_list(int(input('Enter the length of list - ')))
print(A)
print(nearest_element(A, int(input('Enter the number - '))))