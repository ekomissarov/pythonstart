from modul import printlist

#  класс это такое именованное пространство имен
class C:
    pass


print(C)
C.field = "QQ"
print(C.field)


def fun(a):
    return a+a

C.foon = fun
print(C.foon(100500))
printlist(dir(C))


class B:
    var1 = 123
    def fun(self, a):
        print(a+a)


print(B())
ex1 = B()
ex1.fun("qwerty")

#  функция type возвращает класс
a = type(23)("12345") #  равносильно a = int("12345")
#  тип объекта он же класс объекта является конструктором экземляра класса