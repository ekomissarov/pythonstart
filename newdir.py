# учебный скрипт ===

dirList={id(eval(i)):list() for i in dir()}
for i in dir():
    if id(eval(i)) in dirList.keys():
        dirList[id(eval(i))].append(i)

print("{")
for i in dirList: print(i,dirList[i],sep=': ')
print("}")