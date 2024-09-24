from i_abstract_demo import Car, Bike

car1 = Car()
car1.start()
bike1 = Bike()
bike1.start()


# instead of using oops using abs is gud approach
# passing obj
def set_color(obj, col_name):
    obj.color = col_name
    obj.start()  # duckTyping


set_color(car1, "red")
print(car1.color)
set_color(bike1, "Black")
print(bike1.color)
