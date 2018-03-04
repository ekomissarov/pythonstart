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

l = [1]
s = 1
y=''

while len(l)<10:
    x = str(l[len(l) - 1]) + 'Q'
    for i in range(len(x) - 1):
        if x[i] == x[i + 1]:
            s += 1  # счетчик количества одинаковых цифр
        else:  # как только цифры не совпадают, возвращаем счетчик к исходному состоянию сохраняем рез-т
            y += str(s)+str(x[i])
            s = 1  # для последнего значения "Q" счетчик возвращается в 1

    l.append(int(y))
    y = ''

print(l) # A005150
