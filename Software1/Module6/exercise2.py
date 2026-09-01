list=[]
command=input("Enter a number: ")



while command !="":
    num=float(command)
    list.append(num)
    list.sort(reverse=True)
    command=input("Enter a number: ")
        
print(f"The greatest numbers in descending order: ")
if len(list) <5:
    for i in range(len(list)):
        print(list[i])
else :
    for i in range(5):
        print(list[i])