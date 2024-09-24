from g_oop_obj import User, Student, Teacher, Set_Teacher,Stud_fac

user1 = User("naveen", "1989")
user2 = User("Deva", 2003)
user1.reg().log()  # Method Chaining
user2.log()
user1.greet()
print(user1.user_name)
print(User.users)

std = Student("Deepak", 1234,"CSE",90000)
std.log()
std.greet()
print(std.user_name)
print(std.course)
tr = Teacher("DB", 7767)
tr.greet()

st = Set_Teacher("nirmal", 999)
st.greet()

sf = Stud_fac("Ranjani","2021","B.ed","4000")
sf.greet()
