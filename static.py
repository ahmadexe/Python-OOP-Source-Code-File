class Employee:
    def __init__(self, fn, ln, sal):
        self.fname = fn
        self.lname = ln
        self.salary = sal

   
    @staticmethod
    def isopen(day):
        if day.lower() == "sunday":
            print("You don't have to come") 

        else:
            print("Please come")
   
Ahmad = Employee("Ahmad", "Muhammad", 100000)
Employee.isopen("Monday")
Ahmad.isopen("Sunday")
print(Ahmad.salary)