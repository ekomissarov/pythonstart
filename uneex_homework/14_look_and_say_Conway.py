'''
Написать генератор цифр последовательности Конвея «Look and Say».
https://oeis.org/A005150
(Сама последовательность Конвея https://oeis.org/A034002).
Ввести N⩾0 и вывести N-ю цифру последовательности.

Input:

100500
Output:

2
'''

def generat_conoway(seed):
    yield seed
    l = [int(seed)]
    s = 1
    y=''

    while True:
        x = str(l[len(l) - 1]) + 'Q'
        for i in range(len(x) - 1):
            if x[i] == x[i + 1]:
                s += 1  # счетчик количества одинаковых цифр
            else:  # как только цифры не совпадают, возвращаем счетчик к исходному состоянию сохраняем рез-т
                y += str(s)+str(x[i])
                yield s
                yield x[i]
                s = 1  # для последнего значения "Q" счетчик возвращается в 1

        l.append(int(y))
        y = ''

    # print(l) # A005150


N = int(input("Введите N: "))

j = 0
for i in generat_conoway(9):
    N -= 1
    if N < 0:
        print("шаг {} цифра: {}".format(j, i))
        break
    j += 1

