command=float(input("Enter a number (or press Enter to quit):"))

smallest=command
largest=command

while command != "Enter":
    command=float(command)
    if command < smallest:
        smallest= command
    elif command > largest:
        largest= command
    command=input("Enter a number (or press Enter to quit):")
print(f"Smallest number: {smallest:.0f}")
print(f"Largest number: {largest:.0f}")