n = 5
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()
print("\n")
# increasing tri
for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    print()
print("\n")
# decreasing tri
for i in range(n):
    for j in range(i,n):
        print("*", end=" ")
    print()
print("\n")

# right side tri
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for r in range(i+1):
        print("*",end=" ")
    print()
print("\n")

# left side tri
for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for r in range(i,n):
        print("*",end=" ")
    print()
print("\n")

# hill pattern
for i in range(n):
    for j in range(i,n):
        print("  ",end="")
    for r in range(i):
        print("* ",end="")
    for r in range(i+1):
        print("* ",end="")
    print()

print()
for i in range(n):
    for j in range(i+1):
        print("  ",end="")
    for j in range(i,n):
        print("* ",end="")
    for j in range(i,n-1):
        print("* ",end="")
    print()

# number pattern
p=1
for i in range(n):
    for j in range(i+1):
        print(p,end=" ")
    p+=1
    print()

p=1
for i in range(n):

    for j in range(i+1):
        print(p,end=" ")
        p += 1
    print()
print()
for i in range(n):
    p = 1
    for j in range(i+1):
        print(p,end=" ")
        p += 1
    print()
print()

for i in range(n):


    for j in range(i+1):
        print(" ",end=" ")

    p = 5
    for j in range(i,n):
        print(p,end=" ")
        p -= 1
    print()

print()

k=5
for i in range(n):
    p=k
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n):
        print(p,end=" ")
        p -= 1
    k-=1
    print()