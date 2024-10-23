class Parent:
    @staticmethod
    def hello():
        print('hello')

    def hi(self):
        print('hi')
        print(self)

    @classmethod
    def wow(self):
        print('wow')
        print(self)



Parent.hello()
p = Parent()
p.wow()
p.hi()
