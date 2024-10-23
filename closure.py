def outerFunction(message):
    def innerFunction():
        print(message)
    return innerFunction

f = outerFunction('hello')
f()
f1 = outerFunction('hey')
f1()
f()

