class Employee:
    def __init__(self, fn, ln, sal):
        self.fname = fn
        self.lname = ln
        self.salary = sal

   
   
class Engineer(Employee):
    def __init__(self, fn, ln, sal, proglang, exp):
        super().__init__(fn, ln, sal)
        self.programming_language = proglang
        self.experience = exp

Ahmad = Engineer("Ahmad", "exe", 100000000, "Python", 100)
print(Ahmad.salary)
print(Ahmad.programming_language)