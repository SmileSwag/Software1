def get_season(month):

    if month in [12, 1, 2]:
        print(f"The season is winter.")
        return 
    elif month in [3, 4, 5]:
        print(f"The season is spring.")
        return 
    elif month in [6, 7, 8]:
        print(f"The season is summer.")
        return 
    elif month in [9, 10, 11]:
        print(f"The season is autumn.")
        return 
    else:
        print(f"Please enter a number between 1 and 12.")
        return

command=input("Enter the number of a month (1-12): ")	
print(f"You entered: {command}")
get_season(int(command))