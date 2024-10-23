d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(d.items())
print(d.values())
print(d.keys())
d.clear()
print(d)

d1 = {'a': 1, 'b': 2, 'c': 1}
d2 = {'d': 1, 'a': 2, 'c': 1}
d = {**d1, **d2} # concate two dictionary
d1.update(d2) # concate without new dictionary
print(d)
