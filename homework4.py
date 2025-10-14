number = 1
while number <= 1000:
    number += 1
    if number % 3 == 0:
        print(number)


inch = 0
while True:
    inch = int(input("Enter an inch: "))
    centimeter = inch * 2.54
    if inch >= 0:
        print(f"it is {centimeter:.2f} centimeters")
    if inch < 0:
        print("invalid value")
        break



smallest = 0
biggest = 0
while True:
    number = input("Enter a number (or press Enter to quit): ")
    if number == "":
        break
    number = int(number)
    if smallest == 0 or number < smallest:
        smallest = number
    if biggest == 0 or number > biggest:
        biggest = number
print("The smallest number is:", smallest)
print("The biggest number is:", biggest)


import random
target_num = random.randint(1, 10)
user_num = 0
while user_num != target_num:
    user_num = int(input("Guess what the number is: "))
    if user_num == -1:
        break
    elif user_num > target_num:
        print("Too high!")
    elif user_num < target_num:
        print("Too low!")
    else:
        print("Correct!")
print("Game ended")


username = "python"
password = "rules"
attempts = 0
while attempts < 5:
    username1 = str(input("Enter your username: "))
    password1 = str(input("Enter your password: "))
    attempts += 1
    if username1 == username and password1 == password:
        print("You successfully logged in!")
        break
    if username1 != username and password1 != password:
        print("Try again.\n")
if attempts == 5:
    print("access denied.")


N = int(input("How many random points to generate? "))
inside_circle = 0
for i in range(N):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 < 1:
        inside_circle += 1
pi = 4 * inside_circle / N
print("Approximation of π is:", pi)