# task 1
import random
def dice_roll():
    return random.randint(1, 6)

def main():
    total = 0
    while total != 6:
        total = dice_roll()
        print(total)
main()
#
# task 2
import random
def dice_roll2(sides):
    return random.randint(1, sides)


def main2():
    sides = int(input("How many sides do you want? "))
    total = 0
    while total != sides:
        total = dice_roll2(sides)
        print(total)
main2()

#  task 3
def idk(gal):
    gal_to_lit = gal * 3.785
    return gal_to_lit

def main3():
    gal = float(input("How much gallons do you want? "))
    while gal > 0:
        liters = idk(gal)
        print(f"you got {liters:.2f} liters")
        break
main3()

 # task 4
def sub(list):
    idk2 = 0
    for idk3 in list:
        idk2 += idk3
    return idk2

def main4():
    list = [3, 5, 8, 11, 20]
    total = sub(list)
    print(total)
main4()

 # task 5
def sub1(original_list):
    even_numbers = []
    for idk3 in original_list:
        if idk3 % 2 == 0:
            even_numbers.append(idk3)
    return even_numbers

def main5():
    original_list = [3, 5, 8, 11, 20]
    print(sub1(original_list))
    print(original_list)
main5()

# task 6
def idk4(diameter_cm, price_euro):
    diameter_m = diameter_cm / 100
    radius_m = diameter_m / 2
    area = 3.14 * (radius_m ** 2)
    value = price_euro / area
    return value

def main6():
    diameter1 = int(input("Enter the diameter of the pizza "))
    price1 = int(input("Enter the price of the pizza "))
    diameter2 = int(input("Enter the diameter of the pizza "))
    price2 = int(input("Enter the price of the pizza "))
    unit1 = idk4(diameter1, price1)
    unit2 = idk4(diameter2, price2)
    print(f"{unit1:.2f}")
    print(f"{unit2:.2f}")
    if unit1 < unit2:
        print("Pizza 1 offers more value")
    elif unit2 < unit1:
        print("Pizza 2 offers more value")
    else:
        print("Both pizzas have the same value")
main6()