import random

def guess_the_num():
    print(__name__)
    guess = int(input("\nenter ur num: "))
    num = random.randint(1, 20)
    while num != guess:
        if num < guess:
            print("ur guess is greater")
        else:
            print("ur guess is lesser")
        guess = int(input("enter again: "))

    print("You Won!")
guess_the_num()