# Задача 8:
# Требуется определить, можно ли от шоколадки 
# размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no

import os
def clear(): return os.system('cls')
clear()

n = int(input("Enter number N:"))
m = int(input("Enter number M:"))
k = int(input("Enter number K:"))
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('YES')
else:
    print('NO')