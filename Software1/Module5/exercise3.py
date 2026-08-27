command=input("Enter a number (or press Enter to quit): ")
if command!="":
    num=float(command)
    smallest=num
    largest=num
while command!="":
    num=float(command)
    if smallest>num:
        smallest=num
    elif largest<num:
        largest=num
    command=input("Enter a number (or press Enter to quit): ")
print(f"Smallest number: {smallest}")
print(f"Largest number: {largest}")