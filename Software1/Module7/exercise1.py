import random
def roll_dice():
    result=0
    while result!=6:
        result=random.randint(1,6)
        print(result)
    return

roll_dice()


