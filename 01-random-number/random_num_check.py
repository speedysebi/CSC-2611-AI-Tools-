import random
import array

same_num = False
user_num = int(input("Enter a number between 1-10: "))

random_num = [random.randint(1,10) for i in range(5)]

for i in range(random_num):
    if user_num == i:
        print("twinnnnnnnn")
        same_num = True
