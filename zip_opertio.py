
items = [1,2,3,4,5]
prod = ["navee","deva","deepak"]
x= list(zip(items,prod))
print(x)
# zip file always binds tuples into list (list of tuples)
item1 = [1,2,3,4,5]
prod1 = {"navee":21,"deva":22,"deepak":23}
y= list(zip(item1,prod1.items()))
print(y)


import itertools  # for handling variable length
item2 = [1,2,3,4,5]
prod2 = {"navee":21,"deva":22,"deepak":23}
_rd = ["pytho","c","c++","java"]
z= list(itertools.zip_longest(item2,prod2.items(),_rd ,fillvalue="none"))
print(z)

