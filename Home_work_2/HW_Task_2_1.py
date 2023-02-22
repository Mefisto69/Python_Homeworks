# Задача 10:
#  На столе лежат n монеток. Некоторые из них лежат вверх решкой, а
# некоторые – гербом. Определите минимальное число монеток, которые нужно
# перевернуть, чтобы все монетки были повернуты вверх одной и той же
# стороной. Выведите минимальное количество монет, которые нужно
# перевернуть.

import os
clear = lambda: os.system('cls')
clear()

total_coins = int(input('Enter the number of coins: '))
count_tails = 0
count_heads = 0
for i in range(total_coins):
    tails = int(input('heads(1) or tails(0)?'))
    if tails == 0:
        count_tails += 1
    else:
        count_heads += 1
if count_heads > count_tails:
    print(f'flip {count_tails} coins')
else:
    print(f'flip {count_heads} coins')
