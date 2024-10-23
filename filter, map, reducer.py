from functools import reduce

l = [1, 2, 3, 4, 5, 6]
a = list(filter(lambda x: x % 2 == 0, l))
print(a)

b = list(map(lambda x: x + 2, l))
print(b)

c = reduce(lambda x, y: x + y, l)
print(c)
