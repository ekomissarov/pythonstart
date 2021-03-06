'''
Пользуясь формулой Лейбница для вычисления числа Пи:

pi/4 = 1/1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11

написать бесконечный генератор pigen(), возвращающий последовательно
 4, 4-4/3, 4-4/3+4/5, …;
 ввести некоторое расстояние E
 и вывести номер элемента этой последовательности,
 первым попадающего в E/2-окрестность числа Пи.

 Внимание! Тесты написаны из расчёта, что проверка такая:
 как только очередное значение pigen() по модулю перестанет
 отличаться от предыдущего значения больше, чем на E,
 выводим, на каком обороте цикла это произошло.

Input:

0.001
Output:

2000
'''

import itertools

def pigen():
    pi = 0
    d = 1
    for i in itertools.count(start = 1, step = 2):
        pi += d*4/i
        d *= -1
        yield pi


E = float(input("Введите точность E: "))


i_old = 0
step = 1
for i in pigen():
    if abs(i-i_old) < E:
        print("текущее: {} предыдущее: {} шаг: {} err: {}".format(i, i_old, step, abs(i-i_old)))
        break

    if not step%10000000:
        print("текущее: {} предыдущее: {} шаг: {} err: {}".format(i, i_old, step, abs(i-i_old)))

    i_old = i
    step += 1

