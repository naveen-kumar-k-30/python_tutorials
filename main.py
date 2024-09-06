import copy
import math
import random

# import NumGuess
'''
# string method
msg = "hello world"
quote = '"helo"'
print(quote)
print(msg.upper())
print(msg.title())
print(msg + " " + quote + "\n new word\'s\t91729@#@$#%")
print(len(msg))
print(msg.find('w'))  # it returns the index
print(msg.replace('hello', 'allow'))
print((msg+" ") * 4)
'''
print("\n---------------multiple assignments------------------\n")
'''
# multiple assignments
name, age, roll = "naveen", 21, "CSE"
print(name, age, roll, end=" ")
'''
print("\n----------------type casting-----------------\n")
'''
# Type casting
otp = 7939
print(type(otp))
otp = str(otp)
print(type(otp))

c = round(20.9)
print(type(c))
print(c + 1)
'''
print("\n----------------Assignment1-----------------\n")
'''
name1, age1, year = "naveen", 21, 2003
print("Dear " + name1 + "\n You are " + str(age1) + "\n Year " + str(year))
print("\n----------------User input-----------------\n")
what = input("enter ur name: ")
print(what)
h = float(input("enter ur height: "))
print("ur height is " + str(h) + " cm")
h1 = h / 2.54
print("ur h in inches " + f"{h1:.2f}" + " tall")
'''

print("\n---------------function of math------------------\n")
'''
a = -5.44
b = 6
print(round(a), abs(a), pow(a, 2), min(a, b), max(a, b))
a = 2.5
b = 10
x = 4
print(math.ceil(a), math.floor(a), math.factorial(4), math.gcd(x, b))
# ceil - round off, floor- round off,
'''
print("\n----------------assignment 2-----------------\n")
# n = 5
# print(math.log2(n), math.cos(n), math.exp(n))
print("\n-------------relational,logical opt-------------\n")
# < , > , <= , >= , == , != return boolean value
# and or not are logical opt

print("\n----------------Bitwise opt-----------------\n")
'''
& - and, | - or ,~ - not ,^- xor(same - 0 ,diff -1) , >> - left shift(double the value) , << - right shift(value /2)  
'''
print("\n----------------string slicing-----------------\n")
'''
s = "happy"
for i in range(len(s) + 1):
    print(s[:i], end="\n")
for i in range(len(s) + 1):
    print(s[-i:], end="\n")
'''
print("\n----------------list-----------------\n")
# slicing also used in list
'''
l = list(map(int, input().strip().split()))  # to get integer value
print(l)
r = list(input().strip().split())  # to get string values
print(r)

li = ["naveen", 22, "CSE", "saec", "single", "maduravoyal"]
# Modify
li[1] = 21
# Append
li.append("single")
# Insert
li.insert(2, 22)
# Delete
del li[1]
# POP
v = li.pop(3)  # use by index or else it del last
print(v)
# remove
li.remove("single")  # remove by value
print(li)
# temporary sort
l = [5, 3, 7, 2, 8, 9]
print(sorted(l))
print(l)
# permanent sort
l.sort()
print(l)
# reverse
li.reverse()
print(li)
# print(list1[:2])
# print(list1[-1:])
# print(list1[::2])
'''
print("\n----------------Loops-----------------\n")
'''
char = ' '  # space no an alpha
while not char.isalpha():
    char = input("enter the string: ")
print("u entered string: " + char)

'''

# for loop
# for i in range(1, 11, 2):
#     print(i, end=" ")
'''    
print("\n----------------number guess-----------------\n")
# number guess
guess = int(input("\nenter ur num: "))
num = random.randint(1, 20)
while num != guess:
    if num < guess:
        print("ur guess is greater")
    else:
        print("ur guess is lesser")
    guess = int(input("enter again: "))

print("You Won!")
'''

# NumGuess.guess_the_num()
print("\n----------------factors of n-----------------\n")
# factors of n
'''
num = int(input("\nenter ur num: "))
for i in range(1,num+1):
    if num%i == 0:
        print(i,end=" ")
'''
print("\n----------------todo list-----------------\n")
# work =list(input("\nenter ur task ").split(" "))
# print(work)
print("\n----------------finding max -----------------\n")
# lis = list(map(int, input().split(" ")))
# print(max(lis))
print("\n----------------moving neg val to last-----------------\n")
'''
lis = [-1, 3, -4, 5, -9, 6]
for i in lis:
    if i < 0:
        lis.append(i)
        lis.remove(i)
print(lis)
'''
print("\n----------------split and join-----------------\n")
# without split
'''

'''
stri = "a,b,c,d,e,f"
s3 = ""
s2 = "1,2,3,4,5,6,7"
s1 = []
ch = True
for i in s2:
    if ch:
        s1.append(int(i))
        s3 += "".join(i)
        #  s1.append(i)  to append str value
        ch = False
    elif i == ",":
        pass
        ch = True
print(s1)
print(s3)
print("\n----------------2d list copy formats-----------------\n")
'''
skill = ["c", "py", "iot", "cloud", "web"]
#dev = skill #  normal copy would  reflect changes
#dev= skill.copy()  #  skill[::] #  shallow copy changes would not not reflect in dev
dev = copy.deepcopy(skill)  # it would not reflect the changes
skill.pop(2)
print(skill)
print(dev)
nav = ["naveen", 22, "cse"]
mad = ["madhu", 21, "it"]
clg = [nav, mad, dev]
print(clg[2][2])
'''
print("\n----------------tuples-----------------\n")
'''
tup = tuple(map(int,input().split(" ")))
print(tup)
print(tup.index(2))
print(tup.count(3))
print(tup[2])
#it also supports  the 2d ,3d..tuple 
'''
print("\n----------------Dictionary-----------------\n")
'''
dist = {'name': 'naveen', 'age': 21}  # order may change
#  access through index
print(dist['age'])
# adding another item
dist['city'] = 'chennai'
print(dist)
# modify
dist['age'] = 22
# del dist['city']
print(dist)
# printing via pairs
for i, j in dist.items():
    print("key :" + i)
    print("val :" + str(j))
for i in dist.keys():
    print("key: " + i, end=" ")
for i in dist.values():
    print("val: " + str(i), end=" ")
'''
# list of dict
'''
user = []
dist1 = {'name': 'naveen', 'age': 21}
# list in dict
dist1['skill'] = ['c','py','iot','web']
user.append(dist1)
dist2 = {'name': 'madhu', 'age': 21}
user.append(dist2)
print(user)
print(dist1['skill'][2])
'''
print("\n----------------set-----------------\n")
'''
# set
skill = {'py', 'c', 'c++', 'c'}  # set avoid duplicates
print(skill)
l=[1,2,3,3,4,4,5]
m=set(l)
print(m) 
'''

print("\n----------------string formatting-----------------\n")
'''
name = 'Naveen'
like1 = 'apple'
like2 = 'banana'
print("{} likes {} and {}".format(name,like1,like2))
print("{0} likes {2} and {1}".format(name,like1,like2))
print("*****{}*****".format("welcome"))
print("*****{msg:<20}*****".format(msg="welcome"))
print("*****{:>20}*****".format("welcome"))
print("*****{:^20}*****".format("welcome"))
'''
print("\n---------------num formatting-----------------\n")
'''
pi = 3.14567
print("the value of pi is " + f"{pi:.2f}")
num = 1000000
print("the value of num is {:,}".format(num))
a = 24
print("the value of num is {:b}".format(a))  # binary
print("the value of num is {:o}".format(a))  # octal
print("the value of num is {:x}".format(a))  # hexa
'''
print("\n--------------functions-------------------\n")
'''

def fname():
    print("hi")


fname()


def sum(num):
    r = num + num
    return (r)


p = sum(20)
print(p)

'''
print("\n----------------scope of variable-----------------\n")
# num = 10  # global var
# def mad(name):  # local var
#     print("ur name"+name)
#     print(num)
# mad("madhu")
print("\n----------------variable argument-----------------\n")

#
# def sum(*args):  # now we can send multiple  arguments *is the matter here it brings the tuple
#     s = 0
#     for i in args:
#         s += i
#     return s
#
#
# print(sum(25, 25, 25))
print("\n----------------keyword args variable-----------------\n")

def addr_details(**kvargs):
    for k, v in kvargs.items():
        print(v)


addr_details(door_no="11", street="3rd", area="abirami nagar")
print("\n----------------default args-----------------\n")
# def dfv(fname,lname="ram"):  #default val must starts from last pos
#     print("hello"+fname+lname)
# dfv("naveen")  #when value doesn't get means it will use default val
print("\n----------------passing list-----------------\n")
# def print_list(ll):
#     for i in ll:
#         i=i.title()
#         print(i)
# name = ["my","name","is","billa"]
# print_list(name)
# print(name)

print("\n----------------copy concept-----------------\n")

# def print_list(ll):
#     for i in range(0,len(ll)):
#         ll[i]=ll[i].title()
#         print(ll[i],end=" ")
# name = ["my","name","is","billa"]
# print_list(name[:])  #it will not copy it will create another list
# print(name)
# print_list(name)   #it will copies the original list ref
# print(name)
print("\n----------------returning dictionary-----------------\n")
# def user_Info():
#     user={"name":"naveen","age":21}
#     return  user
# user1=user_Info()
# print(user1)
print("\n----------------Recursion-----------------\n")
#fact
# def fact(n):
#     if n==0:
#         return 1
#     return n*fact(n-1)
# fac=3
# print(fact(fac))
# print(math.factorial(3))
print("\n----------------generators-----------------\n")
def sq_num(n):
    for i in range(1,n+1):
        yield i*i
sqn=sq_num(5)  #not to use as list(sq_num) because it not use to use generator list consumes memory but generator don't
for i in sqn:
    print(i,end=" ")
print("\n----------------Modules-----------------\n")
# import test as t
# #from test import otp  or from test import *
# print(t.otp())
print("\n----------------exception handling-----------------\n")
# try:
#     n=int(input("enter the numera: "))
#     m = int(input("enter the dumera: "))
#     d=n//m
#
# except Exception  as e:
#     print("error occured")
#     print(e)
# else:
#     print(d)
# finally:
#     print("hello")
print("\n----------------file opt-----------------\n")
# with open("myfile.txt") as f:
#     print(f.read())  # auto close occur
# print(f.closed)
# txt="I'm ironman"
# with open("myfile.txt",'w') as f:
#     f.write(txt)
# with open("myfile.txt") as f:
#     print(f.read())
# txt_Line=["\nI'm ironman\n","Tony\n","RDJ"]
# with open("myfile.txt",'a') as f:
#     f.writelines(txt_Line)  # writes multiple lines
# with open("myfile.txt") as f:
#     print(f.read())
print("\n----------------walrus Operator-----------------\n")
#syntax := is used to assign and print
list_num = list()
while (i := input()) !='z':
    list_num.append(int(i))
print(list_num)
print("\n----------------Higher order funct-----------------\n")
# it takes functions as parameter or returns a function

#
# def calm_down():
#     print("chill")
#
#
# def happy():
#     print("HAppy hAAPPY ")
#
#
# joy = happy
# print(joy)  # it prints and copying address of happy funct
#
#
# # also we can call like
# def call_ano(fun):  # fun = happy
#     fun()
#     return calm_down
#
#
# check1 = call_ano(happy)
# check1()
print("\n----------------lambda funct-----------------\n")
# normal
# def add_10(n):
#     return n+10
# print(add_10(8))

# lambda
# syntax lambda arg : exp
add_10 = lambda x:x+10
print(add_10(5))

product = lambda x:x*10
print(product(50))
#
# sum = lambda x,y,z:(x*100+y*10+z)
# print(sum(5,2,3))
#
# strong = lambda x: "yes" if x>60 else "no"
# print(strong(65))

# sorting with key

items = [(300, "ss", 5), (234, "pen", 2), (250, "eraser", 1), (434, "mm", 3)]
print("Original list of items:", items)

# Sort the list and store it back in 'items'
items.sort()  # Use 'sort()' without reassigning
print("Sorted items by the first element:", items)

x = [1, 3, 2, 3, 4]
x.sort()  # Sort the list in place
print("Sorted x:", x)
print("mine")
# Sort 'items' by the third element of each tuple
items.sort(key=lambda item: item[2])
print("Sorted items by the third element:", items)
items = [(300, "ss", 5), (234, "pen", 2), (250, "eraser", 1), (434, "mm", 3)]
print("Original list of items:", items)

# Sort the list and store it back in 'items'
items.sort()  # Use 'sort()' without reassigning
print("Sorted items by the first element:", items)

x = [1, 3, 2, 3, 4]
x.sort()  # Sort the list in place
print("Sorted x:", x)

# Sort 'items' by the third element of each tuple
items.sort(key=lambda item: item[2],reverse=True)
print("Sorted items by the third element:", items)

tup_item = ((300, "ss", 5), (234, "pen", 2), (250, "eraser", 1), (434, "mm", 3))
# items.sort()  # tuple can't be modify
# sort - list ,sorted - list,tup..
print(sorted(tup_item))
print(sorted(tup_item,key=lambda i:i[2]))
print(sorted(tup_item,key=lambda i:i[2],reverse=True))

