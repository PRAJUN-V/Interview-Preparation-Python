d1 = {'name': 'Prajun', 'age': 23}
d2 = {'place': 'Madathumbagam'}
# d = {**d1, **d2} # very helpful...
d2.update(d1)
print(d2)
print(**d1)
