class Employee:
    def __init__(self, fn, ln, sal):
        self.fname = fn
        self.lname = ln
        self.salary = sal

    def __add__(self, other):
        return self.salary+other.salary

Ahmad = Employee("xnsakc", "jbcsa", 100)
Haider = Employee("a", "caj", 200)


print(Ahmad+Haider)