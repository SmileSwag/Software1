import random
num=random.randint(0,10)
guess=float(input("Guess a number (1-10): "))
while guess!=num:
    if guess<num:
        print("Too low.")
    elif guess>num:
        print("Too high.")
    guess=float(input("Guess a number (1-10): "))
print("Correct")
