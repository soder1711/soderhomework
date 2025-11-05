season = ["spring", "summer", "autumn", "winter"]
season1 = int(input("Enter the month: "))
if season1 in (9, 10, 11):
    print("The month is", season[2])
elif season1 in (3, 4, 5):
    print("The month is", season[0])
elif season1 in (6, 7, 8):
    print("The month is", season[1])
elif season1 in (12, 1, 2):
    print("The month is", season[3])
else:
    print("Incorrect. This month does not exist")



names = set()
while True:
    names2 = input("Enter names: ")
    if names2 == "":
        for names2 in names:
            print(names2)
        break
    elif names2 in names:
        print("Existing name")
        print(names)
    else:
        names.add(names)
        print(names2, "is added to the list of names")
        print(names)



airports = {}
while True:
    print("\nChoose an option:")
    print("1 to Enter a new airport")
    print("2 to Fetch airport information")
    print("3 to Quit")
    choice = input("Your choice: ")
    if choice == "1":
        icao = input("Enter ICAO code: ").upper()
        name = input("Enter airport name: ")
        if icao in airports:
            print("This airport is already stored.")
        else:
            airports[icao] = name
            print("Airport saved!")
    elif choice == "2":
        icao = input("Enter ICAO code to search: ").upper()
        if icao in airports:
            print(f"The airport is: {airports[icao]}")
        else:
            print("Airport not found.")
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")
