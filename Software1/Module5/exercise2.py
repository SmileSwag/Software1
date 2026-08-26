while True:
    inch=float(input("Enter length in inches (negative value to quit): "))
    centimeter=2.54 * inch
    if inch>= 0:
        print(f"{inch} inches is {centimeter} centimeters.")
        if inch< 0:
            print("Program ended.")
            break