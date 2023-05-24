# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# Пример:
#  10 -> 1 2 4 8

print("\033[32m\0")
N = abs(int(input('Введите число N ')))
stop = 0
P = 1
for i in range(N):
    if stop != -1:
        P = P ** i
        if P <= N:
            print(P, end='  ')
            P = 2
        else:
            stop = 1
    else:
        i = N