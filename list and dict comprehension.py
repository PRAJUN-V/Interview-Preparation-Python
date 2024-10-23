l1 = ['a', 'b', 'c', 'd', 'f', 'g']
l2 = [x for x in range(1, 7)]
d = {k: v for (k, v) in zip(l1, l2)}
print(d)
print(list(zip(l1, l2)))
