'''
There are 3 type of methods in a class

1. Regular methods : takes instance as first argument ie self.
2. Class methods : takes cls as first argument, can be use as additional constructure.
3. Static methiods : if you don't want instance or class anywhere in function we can use static method

'''


class Employee:
    hike_percent = 0.4     # This is a class variable and can be shared acrross all the instance

    def __init__(self,first,last,pay):
        self.first = first #this are instance variables
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    #always pass self(Instance) in regular method
    def fullname(self):
        return self.first + ' ' + self.last

    def pay_hike(self):
        return self.pay * self.hike_percent #we should always use self in place of Employee thus we can set hike seperate;y for each instance

    # This is class method and can be used as additional constructor to class.
    @classmethod
    def takes_param_in_hyphen(cls, in_str):
        fname, lname, pay = in_str.split('_')
        return cls(fname,lname,int(pay))

    @classmethod
    def takes_param_in_slash(cls, in_str):
        fname, lname, pay = in_str.split('/')
        return cls(fname,lname,int(pay))

    #Static method does not need cls or self to be passed, but it does logical work of class
    @staticmethod
    def is_working(date):
        if date.weekday() == 6 or date.weekday() == 7:
            return False
        return True  



#Not need to pass instance(), as it will take automatically
emp_1 = Employee('John','Doe',50000)
emp_2 = Employee('Stephin','Hill',60000)

emp_str_1 = 'John_Doe_50000'
emp_str_2 = 'Stephin_Hill_60000'

emp_str_1_slash = 'John/Doe/50000'
emp_str_2_slash = 'Stephin/Hill/60000'

'''
fname, lname, pay = emp_str_1.split('_')
print(fname)
print(lname)
print(pay)

emp_from_str = Employee(fname,lname,pay)
print(emp_from_str.fullname())

#Easiest way to accept such parameter is by Class method
'''

emp1_from_str = Employee.takes_param_in_hyphen(emp_str_1)
print(emp1_from_str.fullname())

emp2_from_str = Employee.takes_param_in_hyphen(emp_str_2)
print(emp2_from_str.fullname())

emp1_from_str_slash = Employee.takes_param_in_slash(emp_str_1_slash)
print(emp1_from_str_slash.fullname())

emp2_from_str_slash = Employee.takes_param_in_slash(emp_str_2_slash)
print(emp2_from_str_slash.fullname())


import datetime
date = datetime.date(2020,8,20)
print(Employee.is_working(date))