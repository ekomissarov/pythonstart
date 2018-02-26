'''
Ввести кортеж целых чисел V, затем число N.
Написать генератор, возвращающий сначала все числа из кортежа
(в порядке следования), не превосходящие его нулевой элемент,
затем все числа, не превосходящие первый, и т. д.
вплоть до последнего элемента.

Вывести N-й элемент этой последовательности, или "NO", если таковой не существует.

Input:

10, 10, 1, 7, 8, 0, 5
10
Output:

7

'''



t = tuple(eval(input("Введите числа через запятую: ")))
n = int(input("Введите n: "))

for j in range(len(t)):
    for i in t:
        if i <= t[j]:
            print (i, end=" ")
print("\n")


# запишем то же в виде однострочного генератора
a = (i for j in range(len(t)) for i in t if i <= t[j])
print(*a, sep = " ")

# вывод результата
print("\n")
a = tuple(i for j in range(len(t)) for i in t if i <= t[j])
print(a[n] if n <= len(a)-1 else "no")

