list=[]
command=input("Enter a number: ")
while command !="":
    num=float(command)
    list.append(num)
    command=input("Enter a number: ")
list.sort(reverse=True)   
print(f"The greatest numbers in descending order: ")
if len(list) <5:
    for i in range(len(list)):
        print(list[i])
else :
    for i in range(5):
        print(list[i])