name=input("Enter your name: ")
age=int(input("Enter your age: "))
print(name)
print(age)
if age <12:
    print("your are a minor")
elif age>=12:
    print(f"Welcome {name}!")
command=input("What do you want me to do? (choose a verb)")
while age >=12:
    if command=="lopeta":
        break
    elif command=="sing":
        print(f"Ok, I will {command} for you.")
        print("la la la")
    elif command=="cook":
        print(f"Ok, I will {command} for you.")
        print("szzsszzszszsssss.....\n Here comes your favorite meal!")
    command=input("What do you want me to do next?")
    print(f"Ok, I will {command} for you.")
