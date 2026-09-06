list=[]
command=input("Enter a number: ")

while command !="":
    num=float(command)
    list.append(num)
    command=input("Enter a number: ")
list.sort(reverse=True)   
print(f"The greatest numbers in descending order: ")

for i in list[:5]:
    print(i)