d1 = {'a': 1, 'b': 2, 'c': 1}
d2 = {'d': 1, 'a': 2, 'c': 3}
d = {}

l = []
# for i in d1.items():
#     if i[0] not in l:
#         l.append(i[0])
#         d[i[0]] = i[1]
#     else:
#         d[i[0]] = d[i[0]] + i[1]
#
# for i in d2.items():
#     if i[0] not in l:
#         l.append(i[0])
#         d[i[0]] = i[1]
#     else:
#         d[i[0]] = d[i[0]] + i[1]

for k,v in d1.items():
    if k in d2:
        d2[k] += v
    else:
        d2[k] = v


print(d2)
