from functools import reduce

l = [1, 2, 3, 4, 5, 6]
sum_value = reduce(lambda x, y: x + y, l)
print(sum_value)
