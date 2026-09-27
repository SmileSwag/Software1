inventory=[]
def add_item():
    item = input("What item do you want to add?")
    inventory.append(item)
    print(f"{item} has been added to the inventory.")

def remove_item():

    item = input("What item do you want to remove?")
    if item in inventory:
        inventory.remove(item)
        print(f"{item} has been removed from the inventory.")
    else:
        print(f"{item} is not in the inventory.")

def view_items():

    if len(inventory) == 0:
        print("The inventory is empty.")
    else:
        print("Inventory items:")
        for item in inventory:
            print(f"- {item}")

def command_menu():
    while True:
        print(f"\n Command Menu")
        print(f"1. Sing")
        print(f"2. Cook")
        print(f"3. Dance")
        print(f"4. Exit to main menu")
        command=input(" What do you want me to do? (1-4)")

        if command=="1":
            print("Ok, I will sing for you.")
            print("la la la")
        if command=="2":
            print("Ok, I will cook for you.")
            print("szzsszzszszsssss.....\n Here comes your favorite meal!")
        if command=="3":
            print("Ok, I will dance for you.")
            print("dancing...")
        if command=="4":
            main_menu()
            break


def main_menu():
    while True:
        print(f"\n Main Menu")
        print(f"1. Add item")
        print(f"2. Remove item")
        print(f"3. View items")
        print(f"4. Command menu")
        print(f"5. Lopeta")

        command = input(" What do you want me to do? (1-5)")

        if command == "1":
            add_item()
        elif command == "2":   
            remove_item()
        elif command == "3":
            view_items()
        elif command == "4":
            command_menu()
        elif command == "5":
            print("Bye!")
            break

name=input("Enter your name: ")
age=int(input("Enter your age: "))
print(f"you entered your name as {name}")
print(f"you entered your age as {age}")
if age <12:
    print("you are a minor")
elif age>=12:
    print(f"Welcome {name}!")
    main_menu()
