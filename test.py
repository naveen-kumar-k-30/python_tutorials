import random
def otp():
    return random.randrange(555,999)
# lis = [-1, 3, -4, 5, -9, 6]
# n=len(lis)
# for i in range(0,n):
#     if lis[i] < 0:
#         lis.append(lis[i])
#         lis.remove(lis[i])
#         n-=1
# print(lis)
# pattern printing
'''

'''
mat = []
num = 4
s = "*"
for i in range(1,num+1):
    if i==1 or i==num:
        print(s*num)
    elif i>1 and i<num:
        print(s+" "*(num-2)+s)
# hallow pyramid
b = 5
m = round(b / 2)
for i in range(0, 6):
    print("*" * i, end="\n")
for j in range(6, 0, -1):
    print("*" * j, end="\n")
n = 1
for m in range(6, 0,-1):
    print(" " * (m - 1) + "*" * n)
    n += 1
r = 1
for s in range(6, 0 ,-1):
    print("*" * (s - 1) + " " * r)
    r += 1
import pywhatkit
# pywhatkit.sendwhatmsg('+91 9884924266',"vanakam bha",19,58)
