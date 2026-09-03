num=int(input("Enter an integer: "))
if num <2:
    print(f"{num} is not a prime number.")

else:
    for i in range(2,num):
        if num%i==0:
            print(f"{num} is not a prime number.")
            break
    else:
        print(f"{num} is a prime number.")