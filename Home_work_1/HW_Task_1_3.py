# Задача 6: 
# Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no

import os
def clear(): return os.system('cls')
clear()

ticket_number = int(input("To find out if a ticket is lucky,\nenter a six-digit number: "))
if ticket_number > 0 and ticket_number < 1000000:
    left_side = (ticket_number//100000)+(ticket_number%100000//10000)+(ticket_number%10000//1000)
    right_side = (ticket_number%1000//100)+(ticket_number%100//10)+ticket_number%10
    if left_side == right_side:
        print("Congratulations! Lucky ticket!")
    else:
        print("Sorry... Not a lucky ticket =(")
else:
    print("ERROR! Enter a six-digit number!")
