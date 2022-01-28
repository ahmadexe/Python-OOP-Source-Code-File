class Employee:
    def __init__(self, fn, ln, sal):
        self.fname = fn
        self.lname = ln
        self.salary = sal

   

    def increase_salary(self, perc):
        self.salary = int(self.salary + (self.salary * perc))

Ahmad = Employee("Ahmad", "Muhammad", 100000)
Haider = Employee("Haider", "Muhammad", 90000)

Ahmad.increase_salary(.5)

print(Ahmad.salary)