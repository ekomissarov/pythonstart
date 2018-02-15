from modul import printlist

print("\n\nCLASS C")

class C:
    pass


def fun(*par):
    print(par)


C.foon = fun

print(C.foon)
C.foon("qwerty")


b = C()
print(b.foon)
b.foon("qwerty")  # внезапно у метода класса есть еще 1 параметр (ссылка на экземпляр)
# это сделано чтобы можно было обращаться к своим собственным полям


print("\n\nCLASS B")
class B:
    var = 100500
    def fun(self, a):
        self.Another = self.var*2+a
        return 42

b = B()
print(*(s for s in dir(b) if not s.startswith("_")))
print(b.fun(33))
print(*(s for s in dir(b) if not s.startswith("_")))  # образовалось еще одно поле Another


print("\n\nCLASS A __INIT__")
class A:
    def __init__(self, start):
        print("инициализация полей в момент создания экземпляра класса")
        self.start = start
        self.Another = 0

    def fun(self, a):
        self.start += 1
        self.Another += a

print(*(s for s in dir(A) if not s.startswith("_")))
a = A(100)
print(*(s for s in dir(a) if not s.startswith("_")))

