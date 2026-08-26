menu_list="Select option\n1. add \n2. subtract \n3.multiply \n0.exit"
selection= input(menu_list)

while selection !="0":
    if selection=="1":
        num1=float(input("Enter first number: "))
        num2=float(input("Enter second number: "))
        result=num1+num2
        print(f"{num1} + {num2} = {result}")
    elif selection=="2":
        num1=float(input("Enter first number: "))
        num2=float(input("Enter second number: "))
        result=num1-num2
        print(f"{num1} - {num2} = {result}")
    elif selection=="3":
        num1=float(input("Enter first number: "))
        num2=float(input("Enter second number: "))
        result=num1*num2
        print(f"{num1} * {num2} = {result}")
    else:
        print("Invalid selection.")
    selection= input(menu_list)