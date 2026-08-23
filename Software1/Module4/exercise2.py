question=input("Enter the cabin class (LUX, A, B, or C): ")
if question == "LUX":
    print("Upper-deck cabin with a balcony.")
elif question == "A":
    print("Above the car deck, equipped with a window.")
elif question == "B":
    print("Windowless cabin above the car deck.")
elif question == "C":
    print("Windowless cabin below the car deck.")
else:
    print("Invalid cabin class.")