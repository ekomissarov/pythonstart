'''

'''


def f1(x):
    def f2():
        def f3():
            return x
        return f3
    return f2

f = f1(100500)
print(f, f.__closure__[0].cell_contents)  # видно что f создана в локальном пространстве имен функции f1

ff=f()
print(ff, ff.__closure__[0].cell_contents)

'''
f1.<locals>.f2.<locals>.f3 сколько глубина этой цепочки?

~1000 (?) это вопрос стека вызовов в питоне. Рекурсия в питоне ограничена! 
хвостовой рекурсии в питоне нету. Гуглить "Гвидо и хвостовая рекурсия"

так что аккуратнее при построении дереьвев и рекурсивном обходе их :)

'''

print(f.__closure__[0] is ff.__closure__[0])

'''
Какие это перспектиыв открывает нам:
- мы можем создавать конструкторы функций 
при этом не очень думая над тем что там происходит с пространством их имен

изготовление функции внутри функции сообразно некоторым параметрам вполне штатная вещь

например мы передаем функцию, а она возвращает производную функции, 
мы вплотную приближаемся к функциональному программированию как таковому

'''


def g1():
    a = 42  # вот это имя a оно глобальное или локальное?

    def g2():
        nonlocal a  # если мы не хотим его отправлять в замыкание, а хотим изменять
        # принадлежит нэймспейсу вызывающей функции
        a += 1
    g2()
    g2()
    g2()
    return a


g = g1()
print(g)

'''
вот это имя a оно глобальное или локальное?
Ни то ни другое оно nonlocal
'''


def h1(x):
    def h2(a):
            return a+x  # замыкание на лицо
    return h2

print(h1(100500).__closure__[0].cell_contents)


def k1(x):
    def k2(a, t = x):
            return a+t  # замыкание на лицо
    return k2

k = k1(100500)
print(k(3), k(5), k(4, 1000))
print(k.__closure__)  # нет тут никакого замыкания
# этой функции не потребовалось замыкание этот объект внутри функции называется t
# см. https://gist.github.com/dmitrysoshnikov/700292

