"""
make the user input a number between 1-10
then make sure that that number is between 1-10

then, generate 5 numbers between 1-10

then check if any of those 5 numbers match the number that the person input
"""
import random

import boolean

#making a boolean
#before the thanks for playing would print until there is a match! would print

match = False
user_num = int(input("Enter a number between 1-10: "))

if user_num < 1 or user_num > 10:
    print("Please enter a number between 1-10")
    exit()

#random # generator
generated_nums = random.randint(1, 10)

#this checks if the num input equals any of the random
for num in range(1, generated_nums + 1):
    if user_num == num:
        print("There is a match!")
        break
    else:
        print("thanks for playing")
        #thanks for playing repeats a lot when there is a match
        #dunno why