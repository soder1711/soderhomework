import random

name = input("What is your name? ")
print("Hello, " + name)
radius = float(input("Enter the radius of the circle: "))
area = 3.14 * radius * radius
print(f"The area of the circle with radius {radius} is: {area:.2f}")
width = float(input("Enter the width of the rectangle: "))
length = float(input("Enter the length of the rectangle: "))
area = 3.14 * width * length
perimeter = 2 * (width + length)
print(f"The area of the rectangle is: {area:.2f}")
print(f"The perimeter of the rectangle is: {perimeter:.2f}")
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))
sum = number1 + number2 + number3
product = number1 * number2 * number3
average = (number1 + number2 + number3) / 3
print(f"The sum of the numbers is: {sum:.2f}")
print(f"The product of the numbers is: {product:.2f}")
print(f"The average of the numbers is: {average:.2f}")
talent = float(input("Enter talents: "))
pound = float(input("Enter pounds: "))
lot = float(input("Enter lots: "))
sum2 = (talent * 20 * 32 * 13.3 / 1000) + (pound * 32 * 13.3 / 1000) + (lot * 13.3 / 1000)
kg = int(sum2)
grams = (sum2 - kg) * 1000
print(f"The weight in modern units: {kg} kilograms and {grams:.2f} grams.")

random_number_1 = random.randint(0,9)
random_number_2 = random.randint(0,9)
random_number_3 = random.randint(0,9)

print(f"The 3-digit number: {random_number_1}{random_number_2}{random_number_3}.")

random_number_4 = random.randint(1,6)
random_number_5 = random.randint(1,6)
random_number_6 = random.randint(1,6)
random_number_7 = random.randint(1,6)

print(f"The 3-digit number: {random_number_4}{random_number_5}{random_number_6}{random_number_7}.")



