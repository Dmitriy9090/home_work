## Задача вывести все степени 2 не превосходящие числа N
n = abs(int(input('Введите число N: ')))
stop = 0
d = 2
for i in range(n):
    if stop != 1:
        d = d ** i
        if d <= n:
            print(d, end=' ')
            d = 2
        else:
            stop = 1
    else:
        i = n