# https://docs.python.org/3/reference/datamodel.html#special-method-names

# Dunder method, go in python library and check how its used, can be usefull for better understanding

class Employee:

    def __init__(self,first,last,pay):
        self.first = first #this are instance variables
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    #always pass self(Instance) in class method
    def fullname(self):
        return self.first + ' ' + self.last

    def __repr__(self):
        return "Employee repr ('{}, {}, {}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return "Employee str ('{}, {}')".format(self.first, self.last)

    def __add__(self, other):
        return self.pay + other.pay

    def __sub__(self, other):
        return self.pay - other.pay


#Not need to pass instance(), as it will take automatically
emp_1 = Employee('John','Doe',50000)
emp_2 = Employee('Stephin','Hill',6000)
emp_3 = Employee('Cory','Wilson',7000)

# print(emp_1)
# print(emp_1.__repr__())
# print(emp_1.__str__())

print(emp_1 + emp_2)
print(emp_1 - emp_2)