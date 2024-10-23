import copy

# shallow copy
l = [1, 2, 3, 4, [5, 6, 7]]
l1 = l.copy()
l[4][0] = 17
l[3] = 100
print(l)
print(l1)

# deepcopy
l2 = [1, 2, 3, 4, [5, 6, 7]]
l3 = copy.deepcopy(l2)
l2[4][0] = 17
l2[3] = 100
print(l2)
print(l3)
