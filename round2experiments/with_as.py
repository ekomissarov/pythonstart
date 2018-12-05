class Demo:
    def __init__(self):
        self.data = [i for i in range(10)]

    def __enter__(self):
        print("Входим в контекст")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Выход из контекста")

    def __iter__(self):
        return iter(self.data)

    def __str__(self):
        return "DEMO OBJECT: {}".format(self.data)


with Demo() as q:
    for i in q:
        print(i)

    print(q)

