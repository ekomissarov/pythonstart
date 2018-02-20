'''
Ввести восемь чисел через запятую — целочисленные координаты 4-х несовпадающих
 точек A1, A2, A3 и A4: X1, Y1, X2, Y2, X3, Y3, X4, Y4.
 Вывести YES, если прямая A1A2 параллельна прямой A3A4 (или совпадает с ней),
 и NO — если не параллельна.

Input:

1,2,7,14,8,8,18,28
Output:

YES
'''

# уравнение прямой в общем виде
# (y1 - y2)x + (x2 - x1)y + (x1y2 - x2y1) = 0

x1,y1,x2,y2,X1,Y1,X2,Y2 = eval(input("X1, Y1, X2, Y2, X3, Y3, X4, Y4: "))

# не обработан случай вертикальных линий, когда знаменатель обращается в 0
tg_alpha1 = -(y1 - y2)/(x2 - x1)
tg_alpha2 = -(Y1 - Y2)/(X2 - X1)

print("Параллельны" if tg_alpha1 == tg_alpha2 else "Не параллельны")
