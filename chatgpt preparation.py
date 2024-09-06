# def even_odd(n):
#     if (n%2==0):
#         print("Even")
#     else:
#         print("Odd")
# a=int(input())
# even_odd(a)
# a=int(input())
# b=int(input())
# if(a>b):
#     print(str(a)+"is greater")
# else:
#     print(str(b)+"is greater")
#Write a program that prints all the numbers from 1 to 100, but for multiples of 3,
# print "Fizz" instead of the number and for multiples of 5 print "Buzz". For numbers that are multiples of both 3 and 5, print "FizzBuzz".
# for i in range(1,30):
#     if(i%3==0 and i%5==0):
#         print("FizzBuzz")
#     elif(i%3==0):
#         print("Fizz")
#     elif(i%5==0):
#         print("Buzz")
#     else:
#         print(i)

#Write a program that takes a number as input and prints its factorial using a loop.
import math
#m=math.factorial(a)
#print(m)
#<________________or__________________>
# def facto(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*facto(n-1)
# a=int(input())
# print(facto(a))
# def max3(a,b,c):
#     if a>b and a>c:
#         print(a)
#     elif b>c:
#         print(b)
#     else:
#         print(c)
# a = int(input())
# b=int(input())
# c=int(input())
# #print(max(a,b,c)) default func
# max3(a,b,c)
#Write a function that takes a list of numbers and returns their sum.
# li=[1,23,4,5,6]
# #print(sum(li)) default fun
# c=0
# for i in li:
#     c+=i
# print(c)
#Write a program that takes a list of numbers and returns a list containing only even numbers.
# li=[1,23,4,5,6]
# eve=[]
# for i in li:
#     if i%2==0:
#         eve.append(i)
# print(eve)
#Write a function that takes a list and returns the largest element.
# li=[1,23,4,5,6]
# print(max(*li))
#Write a function that takes a tuple of numbers and returns a new tuple with each number squared.
# tu=(1,2,3,4,5,6)
# stu=[]
# for i in tu:
#     stu.append(i*i)
# print(tuple(stu))
# tu = (1, 2, 3, 4, 5, 6)
# stu = tuple(i * i for i in tu)
# print(stu)

#Write a program that swaps the first and last elements of a tuple.
# tu = (1, 2, 3, 4, 5, 6)
# ltu = list(tu)
# ltu[0], ltu[-1] = ltu[-1], ltu[0]
# swapped_tu = tuple(ltu)
# print(swapped_tu)


# def word_frequency(sentence):
#     words = sentence.split()  # Split the sentence into words
#     frequency = {}
#
#     for word in words:
#         word = word.lower()  # Convert to lowercase to make the count case-insensitive
#         if word in frequency:
#             frequency[word] += 1
#
#         else:
#             frequency[word] = 1
#
#     return frequency
#
#
# sentence = input("Enter a sentence: ")
# print(word_frequency(sentence))


# def swap_dict(d):
#     swapped = {value: key for key, value in d.items()}
#     return swapped
#
# original_dict = {'a': 1, 'b': 2, 'c': 3}
# swapped_dict = swap_dict(original_dict)
# print(swapped_dict)

#sets
# Creating a set
# fruits = {"apple", "banana", "cherry"}
#
# # Adding an element
# fruits.add("orange")
# print(fruits)
#
# # Set operations
# print(fruits.union({"kiwi", "apple"}))  # Union
# print(fruits.intersection({"banana", "kiwi"}))  # Intersection
# print(fruits.difference({"banana", "kiwi"}))  # Difference

#Write a function that checks if two sets have any elements in common.
# def have_common_elements(set1, set2):
#     return not set1.isdisjoint(set2)
#
# # Example usage:
# set_a = {1, 2, 3, 4}
# set_b = {3, 4, 5, 6}
# set_c = {7, 8, 9}
#
# print(have_common_elements(set_a, set_b))  # Output: True
# print(have_common_elements(set_a, set_c))  # Output: False

#Write a program to remove duplicates from a list using a set
# def remove_duplicates(lst):
#     return list(set(lst))
#
# my_list = [1, 2, 3, 4, 4, 5, 6, 6]
# unique_list = remove_duplicates(my_list)
# print(unique_list)

# import re
# # Matching a pattern
# pattern = r'\d+'  # Matches one or more digits
# text = 'The year is 2024 and the month is 08'
# matches = re.findall(pattern, text)
# print(matches)
#
# # Substituting patterns
# new_text = re.sub(r'\d+', 'XXXX', text)
# print(new_text)

#file management
# Writing to a file
with open("test.txt", "w") as file:
    file.write("Hello, world!")

# Reading from a file
with open("test.txt", "r") as file:
    content = file.read()
    print(content)
