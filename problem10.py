# reverse a nested list
def reverse_nested_list(lst):
    reversed_list = lst[::-1]
    return [reverse_nested_list(item) if isinstance(item, list) else item for item in reversed_list]

l1 = [1, [2, 3], [[4, 5], 6]]
reversed_l1 = reverse_nested_list(l1)
print(reversed_l1)
