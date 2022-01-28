class Parent:
    def printHello(self):
        print("hello from parent")

class Child(Parent):
    # Same method doing different tasks is called method overriding
     def printHello(self):
        print("hello from child")

c = Child()
c.printHello()