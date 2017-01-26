# учебный скрипт ===
# Значения функций по умолчанию (иллюстрация вычасления аргументов один раз, но не при каждом вызове функции)
def grow1(a,b=[]):
    print(id(b),b,type(b), end=' - ')
    b.append(a)
    print(b)

def grow2(a,b=None):
    print(id(b),b,type(b), end=' - ')
    if b==None: b=[]
    b.append(a)
    print(b)
	
def fun1(a,b=7777):
    print(id(b),b,type(b), end=' - ')
    b+=a
    print(b)

def fun2(a,b=None):
    print(id(b),b,type(b), end=' - ')
    if b==None: b=0
    b+=a
    print(b)

	
print("пробуем первую функцию grow:")
grow1(1); grow1(2); grow1(3)
print("пробуем вторую функцию grow:")
grow2(1); grow2(2); grow2(3)

print()
print("пробуем первую функцию fun:")
fun1(100000); fun1(200000); fun1(300000)
print("пробуем вторую функцию fun:")
fun2(100000); fun2(200000); fun2(300000)
