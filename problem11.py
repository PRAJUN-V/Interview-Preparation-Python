# unflatten a 2d list in python

l = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

x = [j for i in l for j in i]


# x = []
# for i in l:
#     for j in i:
#         x.append(j)

print(x)
