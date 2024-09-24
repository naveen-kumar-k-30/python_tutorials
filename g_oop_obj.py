class User:
    users = 0  # class variable

    def __init__(self, user_name, pwd):
        self.user_name = user_name  # instance variable
        self.pwd = pwd  # _pwd means protected var  __pwd means private(Dunder var)
        User.users += 1

    def reg(self):
        print("registering..." + self.user_name)
        return self

    def log(self):
        print("logging..." + self.user_name)
        return self

    def greet(self):
        print("hello user")


class Student(User):  # inheriting User Class
    def __init__(self,user_name,pwd,course,fee):
        super().__init__(user_name,pwd)
        self.course=course
        self.fee=fee
    def greet(self):  # method overriding
        print("Hi "+self.user_name)


class Teacher(User):  # inheriting User Class
    def greet(self):
        print("Hi Teacher")


# multi level
class Set_Teacher(Teacher):  # inheriting User Class
    def greet(self):
        print("hello mm")


# multiple
class Stud_fac(Student, Teacher):
    def __init__(self,user_name,pwd,course,fee):
        super().__init__(user_name,pwd,course,fee)
    def greet(self):
        print("Hello Bed Teacher"+self.user_name)
        print("here is the detail: "+self.course+" "+self.fee)
