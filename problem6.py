# swap keys and values

d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# d1 = {v: k for (k, v) in d.items()}
# print(d.items())

l = list(d.items())
print(l)
d.clear()
for i in l:
    # temp = i
    # del d[i[0]]
    # print(i)
    d[i[1]] = i[0]

print(d)
