## The "What should I have for dinner today?" Generator, by João Carvalho

import random
import time

print("Welcome to the Meal Chooser! I will help you decide on what to eat today. ", "\n")

time.sleep(1)

question = print("You can choose from:", "\n",)

time.sleep(1)

print("Junk Food")
time.sleep(1)
print("Healthy Meal")
time.sleep(1)
print("Surprise Me", "\n")
time.sleep(1)

option_1 = "Junk Food"
option_2 = "Healthy Meal"
option_3 = "Surprise Me"

list_1 = ["A Hamburger!", "A Hot Dog!", "Pizza!", "Lasagna!", "Cannelloni!", "Tacos!"]
list_2 = ["Salad!", "Veggie Bowl!", "Chicken Wrap!"]
list_3 = ["A Hamburger!", "Pizza!", "Lasagna!", "Cannelloni!", "Tacos!", "Salad!", "Veggie Bowl!", "Chicken Wrap!"]

time.sleep(1)

answer = input("Choose 1 for " + option_1 + ", 2 for " + option_2 + " or 3 for " + option_3 + ": ")
print()

if answer == "1":
    print("Your meal will be...", "\n")
    time.sleep(2)
    print(random.choice(list_1), "\n")
    time.sleep(1)
    print("Enjoy your meal, but don't eat this every day!", "\n")
    time.sleep(2)
elif answer == "2":
    print("Your meal will be...", "\n")
    time.sleep(2)
    print(random.choice(list_2), "\n")
    time.sleep(1)
    print("Enjoy your meal! That's a healthy one.", "\n")
    time.sleep(2)
elif answer == "3":
    print("Your meal will be...", "\n")
    time.sleep(2)
    print(random.choice(list_3), "\n")
    time.sleep(1)
    print("Enjoy your meal!", "\n")
    time.sleep(2)
else:
    print("Invalid option. Please choose option 1, 2 or 3 (input just the number).")
    
print("Thank you for using my randomizer! João Carvalho 2023", "\n")
time.sleep(2)
input("Press ENTER to exit.")
