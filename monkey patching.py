class Monkey:
    def hello(self):
        print('hello')

m = Monkey()
def hi():
    print('hi')
m.hello = hi
m.hello()
