class A:
    var = 1

class B:
    def fun(self):
        return 100500

class C(A,B):
    Field = None


a = A()
print(a.__dict__, "\n", A.__dict__)  # var это поле класса
print ([i for i in dir(a) if not i.startswith("__")])

b = B()
print(b.fun())
print ([i for i in dir(b) if not i.startswith("__")])

c = C()
print ([i for i in dir(c) if not i.startswith("__")])

print(issubclass(C, A), issubclass(C, B))
print(isinstance(c,A), isinstance(c,B), isinstance(c,C))

'''
Ситуация когда у родителей есть одинаковые поля, что еще хуже, когда у них есть одинаковые методы
сильно запутаны (описаны в справочнике Лутца)
В некоторых языках типа Java множественное наследование просто запрещено

Упоминалось ромбическое наследование.

Есть некий алгоритм прохода по дереву полей. Простейший обход вот этих полей со словами выживает
то поле, которое мы посмотрели последнее/первое, он не работает в случае замкнутого множества,
потому что некоторая функциональность может приеать из одного класса, а некоторая из другого.
MRO - method resolution order (вообще его можно перебить)

Разумный пример таких наследований привести довольно сложно.
В реальной действительности довольно редко приходится делать ромбическое наследование.


'''
