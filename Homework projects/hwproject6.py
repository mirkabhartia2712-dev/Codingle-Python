number = float(input("Enter a number: "))

if number < 0:
    print("Cannot calculate square root of a negative number")
else:
    square_root = number ** 0.5
    print("The square root of", number, "is", square_root)