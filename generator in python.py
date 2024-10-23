def hello():
    for i in range(10):
        yield i

a = hello()
print(next(a))
print(next(a))
print(next(a))
