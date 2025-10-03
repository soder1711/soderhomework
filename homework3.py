length = int(input("Enter the length of a zander "))
if length < 42:
    print(f"Please release the {length} cm zander back into the lake. \nA zander must be 42 centimeters or longer to meet the size limit.")
elif length > 42 or length == 42:
    print(f"You caught a {length} cm zander!")



cabin = input("Please enter the cabin class of a cruise ship?\nLUX: upper-deck cabin with a balcony.\nA: above the car deck, equipped with a window.\nB: windowless cabin above the car deck.\nC: windowless cabin below the car deck. ")
if cabin in "AaBbCc":
    print("That's a great option!")
elif cabin == "LUX":
    print("That's a great option!")
else:
    print("Invalid cabin class")



gender = input("What is your gender? ")
if gender == "Female" or gender == "female":
    hemoglobin = int(input("Please enter your hemoglobin value "))
    if hemoglobin > 155:
        print("Your hemoglobin value is too high!")
    elif hemoglobin < 117:
        print("Your hemoglobin value is too low!")
    elif 155 > hemoglobin > 117:
        print("Your hemoglobin value is average!")
elif gender == "Male" or gender == "male":
    hemoglobin = int(input("Please enter your hemoglobin value "))
    if hemoglobin > 167:
        print("Your hemoglobin value is too high!")
    if hemoglobin < 134:
        print("Your hemoglobin value is too low!")
    if 167 > hemoglobin > 134:
        print("Your hemoglobin value is average!")
else:
    print("You are not a human, are you?")

year = int(input("Please enter the year "))
if year % 400 == 0:
    print("The year is a leap year.")
elif year % 4 == 0:
    print("The year is a leap year.")
elif year % 100 == 0:
    print("The year is a leap year.")
else:
    print("The year is not a leap year.")

