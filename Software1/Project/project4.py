class Player:
    def __init__(self, name:str , items: list [Item] = [] , location: Room = ''):
        self.name=name
        self.items=items
        self.location=location

    def move(self, destination: Room):
        self.location=destination
        self.collect_item()

    def collect_item(self):
        self.items.append(self.location.item)
        print(f"{self.location.item.name} has been added to the inventory.")

class Room:
    def __init__(self, name: str, item: Item):
        self.name=name
        self.item=item

class Item:
    def __init__(self, name: str , weight: float):
        self.name=name
        self.weight=weight


def remove_item():
    item_name = input("What item do you want to remove?")
    for i in player.items:
        if i.name == item_name:
            player.items.remove(i)


def view_items():
    if len(player.items) == 0:
        print("The inventory is empty.")
    else:
        print("Inventory items:")
        for item in player.items:
            print(f"- {item.name}")

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
        print(f"1. Visit Rooms")
        print(f"2. Remove item")
        print(f"3. View items")
        print(f"4. Command menu")
        print(f"5. Lopeta")

        command = input(" What do you want me to do? (1-5)")

        if command == "1":
            move_to_room()
        elif command == "2":   
            remove_item()
        elif command == "3":
            view_items()
        elif command == "4":
            command_menu()
        elif command == "5":
            print("Bye!")
            break

def move_to_room():
    room_no=input("Which room do you want to go? Enter nummber 1-7")
    item_obj=''
    room_obj=''
    if room_no== "1":
        print("you found a banana")
        item_obj = Item('banana', 0.2)
        room_obj = Room('1', item_obj)
    elif room_no== "7":
        print("you found a knife")
        item_obj = Item('knife', 1)
        room_obj = Room('7', item_obj)
    elif room_no== "5":
        print("you found a gold bar")
        item_obj = Item('gold bar', 4)
        room_obj = Room('5', item_obj)
    else: 
        print("you found nothing")
    player.move(room_obj)



name=input("Enter your name: ")
age=int(input("Enter your age: "))
player=Player(name)
print(f"you entered your name as {name}")
print(f"you entered your age as {age}")
if age <12:
    print("you are a minor")
elif age>=12:
    print(f"Welcome {name}!")
    main_menu()
