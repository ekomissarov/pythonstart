'''

поскольку синтацксис декоратора функции не предусматривает
передачу параметров
типа @deco(1,2) - это вызов функции

значит нам нужен конструктор декораторов, сейчас мы его создадим

'''

def deco(n):  # конструктор декоратора (n залипает в замыкании)
    def dec2(f):  # собственно декоратор принимающий функцию для декорирования
        def fun(*ap, **an):
            print("*"*n)
            return f(*ap, **an)  # вызов декорируемой функции
        return fun
    return dec2


@deco(30)
def fun1(a):
    return a*2+1


dec = deco(30)
print(dec.__closure__, dec.__closure__[0].cell_contents)
@dec
def fun2(a):
    return a*2+2



print(fun1(42))
print(fun2(42))
