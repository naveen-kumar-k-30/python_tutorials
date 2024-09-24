print("Finding a particular number in a list:")


def find_number_in_list(lst, num):
    if num in lst:
        return f"{num} is present in the list."
    else:
        return f"{num} is not in the list."


# Example
my_list = [1, 2, 3, 4, 5]
number = 3
print(find_number_in_list(my_list, number))
print("Check whether an element is present in a list:")


def is_element_in_list(lst, element):
    return element in lst


# Example
my_list = ['apple', 'banana', 'cherry']
element = 'banana'
print(is_element_in_list(my_list, element))
print("Split an n-digit number into list elements:")


def split_number_to_list(n):
    return [int(digit) for digit in str(n)]


# Example
number = 12345
print(split_number_to_list(number))
print("Split a string into a list of characters:")


def split_string_to_list(s):
    return list(s)


# Example
string = "hello"
print(split_string_to_list(string))
print("Check if a particular character is present in a string:")


def is_character_in_string(s, char):
    return char in s


# Example
string = "hello"
character = 'e'
print(is_character_in_string(string, character))
print("list topics")
print("Creation, Indexing, and Slicing")
# List creation
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Accessing the 3rd element
third_element = numbers[2]
print(f"Third element: {third_element}")

# Slicing to get the first 5 elements
first_five = numbers[:5]
print(f"First 5 elements: {first_five}")

# Slicing to get the last 3 elements
last_three = numbers[-3:]
print(f"Last 3 elements: {last_three}")
print(" Adding, Updating, and Removing Elements")

# Initial list of fruits
fruits = ['apple', 'banana', 'cherry']

# Adding a new fruit
fruits.append('orange')
print(f"After append: {fruits}")

# Updating an existing fruit (replace 'banana' with 'mango')
fruits[1] = 'mango'
print(f"After update: {fruits}")

# Removing a fruit ('apple')
fruits.remove('apple')
print(f"After remove: {fruits}")
print("Iterating Through Lists")
# List of numbers
numbers = [1, 2, 3, 4, 5]

# Iterating through the list to print the square of each number
for num in numbers:
    print(f"{num} squared is {num ** 2}")

print("List Comprehensions")
# List comprehension for squares
squares = [x ** 2 for x in range(1, 11)]
print(f"Squares: {squares}")

print("Common List Operations")
# Initial list
numbers = [5, 2, 9, 1, 7]

# Append
numbers.append(10)
print(f"After append: {numbers}")

# Extend
numbers.extend([11, 12])
print(f"After extend: {numbers}")

# Insert at index 2
numbers.insert(2, 6)
print(f"After insert: {numbers}")

# Pop the last element
last_element = numbers.pop()
print(f"After pop: {numbers}, Popped element: {last_element}")

# Remove a specific number (2)
numbers.remove(2)
print(f"After remove: {numbers}")

# Reverse the list
numbers.reverse()
print(f"After reverse: {numbers}")

# Sort the list
numbers.sort()
print(f"After sort: {numbers}")
a = sorted(numbers, reverse=True)
print(f"After sorted in reverse {a}")
print("permanent sort")
numbers = [5, 2, 9, 1, 7]
numbers.sort(reverse=True)
print(f"After sort in reverse: {numbers}")
print("Create a list of integers and find the sum of all elements.")
li = [1, 2, 3, 4, 5]
s = 0
for i in li:
    s = s + i
print(s)
print("Write a program to find the second largest number in a list.")
li.sort(reverse=True)
print(f"second largest number is {li[1]}")
print("Write a function that accepts a list and removes duplicates.")
lis = [1, 2, 3, 3, 4, 4, 5, 6, 6, 7]


def remove_duplicates(lis):
    return list(set(lis))


print(remove_duplicates(lis))
print(" Challenge: List Manipulation")
# Initial list of temperatures in Celsius
temperatures = [15, 22, 18, 30, 25]

# Convert to Fahrenheit
fahrenheit = [(temp * 9/5) + 32 for temp in temperatures]
print(f"Temperatures in Fahrenheit: {fahrenheit}")

# Find the max and min temperatures
max_temp = max(temperatures)
min_temp = min(temperatures)
print(f"Max temp: {max_temp}, Min temp: {min_temp}")

# Filter temperatures greater than 20°C
above_20 = [temp for temp in temperatures if temp > 20]
print(f"Temperatures above 20°C: {above_20}")
print("Bonus Problem: Flatten a Nested List Using List Comprehension")
# List of lists
nested_list = [[1, 2], [3, 4], [5, 6]]

# Flatten the nested list
flattened = [item for sublist in nested_list for item in sublist]
print(f"Flattened list: {flattened}")

print("**********************challenge round*****************************")
##Basic List Operations
# Create a list of the first 15 even numbers.
x=[i for i in range(0,16) if i%2==0]
print(x)
# Access and print the 5th element from the list.
print(x[4])
# Slice and print the last 4 elements of the list.
print(x[-4:])
# Find the Maximum and Minimum
# Given a list of integers, write a function that finds the maximum and minimum values in the list without using the max() or min() functions.
def maxn(lis):
    a=list(set(lis))
    a.sort(reverse=True)
    return a[0]
def minn(lis):
    a = list(set(lis))
    a.sort()
    return a[0]
print(f"max of x is {maxn(x)}")
print(f"min of x is {minn(x)}")
#  Find the Second Smallest Number
# Write a program to find the second smallest number in a list. Your function should handle cases where there are duplicate values.
def sm(lis):
    a = list(set(lis))
    a.sort()
    return a[1]
print(f"2nd smallest of x is {sm(x)}")

# 4. Sum of Even Numbers
# Create a list of integers and write a program to calculate the sum of only the even numbers in the list using a loop.
ll=[1,2,3,4,5,6,7,8,9]
ll1=sum([i for i in ll if i%2==0])
print(f"sum of even numbers{ll1}")

# 5. List Comprehension for Strings
# Given a list of words, use list comprehension to create a new list containing only words that start with the letter 'a'.
words = "apple is a valid thing in a kalki movie"
lwords = words.split(" ")
print(lwords)
awords = [i for i in lwords if i.startswith('a')]
print(f"a letters words: {awords}")
# Merge Two Lists
# Given two lists of integers, write a function that merges them into one list in ascending order. Do not use the built-in sort() function.
l1=[1,2,3,4,5,6]
l2=[7,8,9,10]
l2.extend(l1)
print(l2)
x=list(set(l2))
print(x)
# 8. Reverse a List
# Write a program that reverses a list without using the reverse() function or slicing ([::-1]).
l1=[1,2,3,4,5,6]
l1.sort(reverse=True)
print(l1)
dup=[1,2,2,3,3,4,5,6]
def finddup(dup):
    seek = set()
    dupli = set()
    for i in dup:
        if i in seek:
            dupli.add(i)
        else:
            seek.add(i)
    return list(dupli)
print(finddup(dup))
# 10. List Comprehension for Multiples
# Use list comprehension to create a list of all numbers between 1 and 100 that are divisible by both 3 and 5.
mul35=[i for i in range(1,100) if i%3==0 and i%5==0]
print(mul35)
# 11. Rotate a List
# Write a function that rotates a list by a given number of steps to the right. For example, rotating [1, 2, 3, 4, 5] by 2 steps gives [4, 5, 1, 2, 3].
l1=[1,2,3,4,5]
n=len(l1)
m=n//2
r=[]
for i in range(0,n-m):
    r.append(l1[n-1])
    n=n-1
r.extend(l1[:m])
print(r)
print("********************************")
n=len(l1)
m=n//2
r=l1[-m:]
r.extend(l1[:-m])
print(r)
# 12. Flatten a Nested List
# Given a list of lists (nested list), write a function that flattens it into a single list. For example, [[1, 2], [3, 4], [5, 6]] becomes [1, 2, 3, 4, 5, 6].
l1=[[1, 2], [3, 4], [5, 6]]
x= [i for sub in l1 for i in sub]
print(x)
# 13. Count Occurrences of an Element
# Write a function that takes a list and an element as input, and returns the number of times the element appears in the list.
dup=[1,2,2,3,3,3,4,5,6]
def countduptimes(dup):
    seek=set()
    dupli=set()
    for i in dup:
        if i in seek:
            dupli.add(i)
        else:
            seek.add(i)
    for i in dupli:
        n=dup.count(i)
        print(f"{i} appears {n} times ")
countduptimes(dup)
# Find the Intersection of Two Lists
# Write a function that takes two lists and returns a list containing only the elements that are present in both lists (i.e., the intersection of the two lists).
l1= [1,2,3,4,5,6]
l2=[9,8,7,6,5,4,3]
def samesame(l1,l2):
    l1=list(set(l1))
    l2=list(set(l2))
    s=[]
    for i in l1:
        if i in l2:
            s.append(i)
    return s
print(samesame(l1,l2))
# Zip Two Lists
# Write a program that "zips" two lists together. If one list is longer than the other, discard the extra elements. For example, zipping [1, 2, 3] and [4, 5, 6, 7] would give [(1, 4), (2, 5), (3, 6)].
l1= [1,2,3,4,5,6,9,8,7]
l2=[9,8,7,6,5,4,3]
l3=list(zip(l1,l2))
print(l3)
# Find Unique Pairs: Write a program to find all unique pairs of integers in a list that sum up to a given target number.
def find_unique_pairs(lst, target):
    seen = set()  # To track the numbers we have seen
    pairs = set()  # To store unique pairs

    for number in lst:
        complement = target - number

        if complement in seen:
            # Add the pair as a sorted tuple to ensure uniqueness
            pairs.add((min(number, complement), max(number, complement)))

        seen.add(number)

    return list(pairs)


# Example usage:
numbers = [1, 2, 3, 4, 3, 5, 6, 2]
target_sum = 6
unique_pairs = find_unique_pairs(numbers, target_sum)
print(unique_pairs)  # Output: [(1, 5), (2, 4), (3, 3)]
print("***********   pattern   ***********")
n = 5
for i in range(1, n+1):
    print(" " * (n - i) + "* " * i)

for i in range(n-1,0,-1):  # i = 4,3,2,1
    print(" "*(n-i)+"* "*i)
print("*************** OOPS  *********************")
