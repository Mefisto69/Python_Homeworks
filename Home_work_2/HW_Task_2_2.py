# Задача 12
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа 
# X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

import os
clear = lambda: os.system('cls')
clear()

number_x = int (input('Enter a number Х (≤1000):'))
number_y = int (input('Enter a number Y (≤1000):'))
for i in range(number_x):
    for j in range(number_y):
        if number_x==i+j and number_y==i*j:
            break
print(number_x,number_y)
