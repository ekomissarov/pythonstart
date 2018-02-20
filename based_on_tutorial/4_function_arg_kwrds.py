def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    print(arguments)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    print(keywords)
    for kw in keywords:
        print(kw, ":", keywords[kw])
# аналогично, но без лишней операции индексирования:
    for k, v in keywords.items():
        print(k, ":", v)

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")
