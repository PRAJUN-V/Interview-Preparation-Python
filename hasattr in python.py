class A:
    def __init__(self, name):
        self.name = name

a = A('prajun')
print(hasattr(a, '__str__'))
print(hasattr(a, 'name'))
