''' instance variables are unique to each instance, class variables are shared/same amonst each instance'''

class Employee:
    hike_percent = 0.4     # This is a class variable and can be shared acrross all the instance

    def __init__(self,first,last,pay):
        self.first = first #this are instance variables
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    #always pass self(Instance) in class method
    def fullname(self):
        return self.first + ' ' + self.last

    def pay_hike(self):
        return self.pay * self.hike_percent #we should always use self in place of Employee thus we can set hike seperate;y for each instance

        
#Not need to pass instance(), as it will take automatically
emp_1 = Employee('John','Doe',50000)
emp_2 = Employee('Stephin','Hill',60000)

print(emp_1.pay_hike())
print(emp_2.pay_hike())