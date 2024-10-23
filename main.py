import keyword
import sys
import builtins

# To get keywords in python
# help(keyword)
print(keyword.__all__)
print(keyword.kwlist)
print(keyword.softkwlist)
print(keyword.iskeyword('is')) # True
print(keyword.iskeyword('name')) # False

# To get all the builtin modules in python
print(sys.builtin_module_names)

# List all built-in functions and objects
print(dir(builtins))

# Use dir() to get all attributes and methods of a basic object
magic_methods = [method for method in dir(object) if method.startswith('__') and method.endswith('__')]

# Print the list of magic methods
print(magic_methods)
