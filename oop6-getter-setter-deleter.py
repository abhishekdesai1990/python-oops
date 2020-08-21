# we can use getter setter when we need to change attribute with out creating function

class Employee:
    def __init__(self,first,last,pay):
        self.first = first #this are instance variables
        self.last = last
        self.pay = pay

    #This is getter
    @property
    def email(self):
        return self.first + '.' + self.last + '@company.com'

    @property
    def fullname(self):
        return self.first + ' ' + self.last

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

#Not need to pass instance(), as it will take automatically
emp_1 = Employee('John','Doe',50000)
emp_2 = Employee('Stephin','Hill',6000)

'''
So if we check below we set first name but it does not set in email, here problem arises, to avoid that
we use getters
'''
emp_1.first = 'Corry'
emp_1.last = 'Williams'
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

emp_1.fullname = "Torry james"

print ('-------------------------')

