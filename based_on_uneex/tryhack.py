class A:
    def __add__(self,a):
        return 10000+a

int = A


a=A()
print(a+1)

b=10
print(b+1)

print(type(a))
print(type(b))


print(int is A)
print(id(A.__add__))
print(id(int.__add__))
print(int.__add__ is A.__add__)
