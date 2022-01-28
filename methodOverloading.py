# By defaukt there is no method overloading in python but using classes we can do it in form of method overriding

class alpha:
    def sum(self,a,b):
        return a+b
class beta:  
    def sum(self,x,y,z):
        return x+y+z
a = alpha()
b = beta()
print(b.sum(5, 5, 5))




