numList = tuple(map(int, input().split()))
print(*(i for i in numList if not i%2))
