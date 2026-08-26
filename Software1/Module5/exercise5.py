attempt=0

while attempt !=5:
    username=input("Enter username: ")
    password=input("Enter password: ")
    if username =="python" and password =="rules":
        print("Welcome")
        break
    else:
        print("Please try again.")
    attempt +=1
