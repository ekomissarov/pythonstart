'''
замыкание и декораторы - 12 лекция

Любая питоновская функция это объект
'''

def fun(a):
    return a+a


print(fun, id(fun), dir(fun))
# наличие метода __call__ говорит нам о том что функцию можно вызвать


def ffun(f):
    return f(1), f(2)

print(ffun(fun))  # функция в качестве передаваемого параметра


# мы можем написать функцию, которая конструирует функцию
def constr(n):
    def fun1(a):
        #print(dir(), locals(), globals()) # n "залипает" в пространстве имен fun1 (на самом деле нет)
        print(dir())
        return a*2+n
    return fun1  # вот здесь вообще говоря пространство имен constr перестает существовать
'''
при определении функции питон не выполняет ее тело, но анализирует ее 
содержимое на предмет локальных и глобальных переменных имен и их присваивания
(для того чтобы отличать locals от globals для того чтобы случайно не перебить значения)
- если имя встречается в левой части присваивания значит оно локальное
- если имя объявлено как global оно конечно глобальное

и вот здесь же питон выясняет что имя n специфическое, оно приехало в пространстве имен
locals функции constr оно залипает
то место где n залипнет не имеет отношения к понятию locals или globals
когда мы вызовем fun1 ее пространство имен создастся, когда мы из нее выйдем оно убьется
очевидно n лежит не в fun1

это место где зависло n называется __closure__ / замыкание (поле объекта fun1)
некое пространство имен которое наша функция fun1 видела, когда мы ее определяли 
и которое уничтожится когда это определение произойдет 

'''

print(constr(100500))
g=constr(100500)
print(g(2))

print(*(i for i  in dir(g) if i.startswith("__clo")))
print(type(g.__closure__), g.__closure__, g.__closure__[0].cell_contents) # здесь лежит 100500



