names = set()

while True:
    name = input("Enter a name (or press Enter to finish): ")
    
    if name == "":
        break
    
    if name in names:
        print("Existing name")
    else:
        print("New name")
        names.add(name)

print("\nEntered names:")
for name in names:
    print(name)
