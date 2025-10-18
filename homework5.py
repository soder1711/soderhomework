import random
dice = int(input("how many dice do you want to roll? "))
total = 0
for number in range(dice):
    dice2 = random.randint(1, 6)
    total += dice2
print(total)


biggest = []
while True:
    number1 = input("Please enter the random numbers: ")
    if number1 == "":
        break
    number1 = int(number1)
    biggest.append(number1)
    biggest.sort(reverse=True)
print(biggest[0])
print(biggest[1])
print(biggest[2])
print(biggest[3])
print(biggest[4])


number2 = int(input("Please enter the random number: "))
if number2 < 2:
    print("The number is not a prime number.")
else:
    for idk in range(2, number2):
        if number2 % idk == 0:
            print("The number is not a prime number.")
            break
    else:
        print("The number is a prime number.")


cities = []
for idk2 in range(5):
    action2 = input("Which city do you want to add?: ")
    cities.insert(0, action2)
print("the cities you entered are: ")
for action2 in cities:
    print(action2)

