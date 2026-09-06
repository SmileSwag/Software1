import random
def roll_dice(sides):
    result=0
    while result!=sides:
        result=random.randint(1,sides)
        print(result)
    return
max_sides=int(input("Enter the number of sides on the die: "))
roll_dice(max_sides)