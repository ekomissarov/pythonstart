'''
исключения выполняют 2 ф-ии:
1) это такие ошибки, которые можно обработать

'''


def fun():
    print(zzz)

try:
    fun()
except Exception as e:
    print("Ooops!!", e)


print("QQ")