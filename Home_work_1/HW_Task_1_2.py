# Задача 4: 
# Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, 
# что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
# 6  -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

import os
clear = lambda: os.system('cls')
clear()

Teamwork_S = int(input("Enter a total cranes: "))
Petyas_result = Teamwork_S//3//2
Seryogas_result = Petyas_result
Katyas_result = (Petyas_result + Seryogas_result)*2
print(f"Petya made {Petyas_result} out of {Teamwork_S} cranes,")
print(f"Katya made {Katyas_result} out of {Teamwork_S} cranes,")
print(f"Seryoga made {Seryogas_result} out of {Teamwork_S} cranes.")