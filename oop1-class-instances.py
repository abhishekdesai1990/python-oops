class Employee:
    '''__init__ is a constructor/initiator method of class, first argument should always be self ie instance'''

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    #always pass self(Instance) in class method
    def fullname(self):
        return self.first + ' ' + self.last

#Not need to pass instance(), as it will take automatically
emp_1 = Employee('John','Doe',50000)
emp_2 = Employee('Stephin','Hill',6000)

print(emp_1.first)
print(emp_2.first)

print(emp_1.fullname())
print(emp_2.fullname())