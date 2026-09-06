import math
def calculate_unit_price(diameter,price):
    radius_meter=(diameter/2)/100
    area= math.pi * (radius_meter**2)
    price_meter=price/area
    return price_meter

d1=float(input("Enter the diameter of the first pizza (cm): "))
p1=float(input("Enter the price of the first pizza (euros): "))
d2=float(input("Enter the diameter of the second pizza (cm): "))
p2=float(input("Enter the price of the second pizza (euros): "))
pm1=calculate_unit_price(d1,p1)
pm2=calculate_unit_price(d2,p2)
print(f"Unit price of the first pizza: {pm1:.2f} euros/m²")
print(f"Unit price of the second pizza: {pm2:.2f} euros/m²")
    
if pm1==pm2:
    print("Same price bruh")
elif pm1<pm2:
    print("The first pizza provides better value for money.")
else:
    print("The second pizza provides better value for money.")