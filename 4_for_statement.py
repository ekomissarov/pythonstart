'''
в питоне есть несколько типов данных, вот основные из них:
- тюпль (кортеж)
- список
- множества и словари
В примере ниже используется список. 
Для цикла for объект должен быть иттерируемый https://docs.python.org/3/tutorial/classes.html#iterators
'''

words = ['cat', 'window', 'defenestrate']
print(words)
print(dir(words), '\n\n')
for w in words:
    print(w, len(w))
