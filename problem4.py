# return the key of maximum value
#
# using for loop
d = {'name': 1, 'age': 2, 'school': 3}
values = d.values()
print(values)
max_value = max(values)
print(max_value)
for i in d:
    if d[i] == max_value:
        print(i)

# another method
d = {'name': 1, 'age': 2, 'school': 3}
max_key = max(d, key=d.get)
print(max_key)

