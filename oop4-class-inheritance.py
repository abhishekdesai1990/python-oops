class Employee:
    hike_percent = 0.4     # This is a class variable and can be shared acrross all the instance

    def __init__(self, first, last, pay):
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


class Developer(Employee):
    def __init__(self, first, last, pay, specialization):
        super().__init__(first, last, pay)
        self.specialization = specialization




#Not need to pass instance(), as it will take automatically
emp_1 = Developer('John', 'Doe', 50000, 'javascript')
emp_2 = Developer('Stephin', 'Hill', 60000 , 'python')


print(emp_1.fullname())