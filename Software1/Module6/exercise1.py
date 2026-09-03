import random

command=int(input("How many dice to roll: "))
sum=0

for i in range(command):
    sum+=random.randint(1,6)
print(f"Sum of the dice: {sum}")