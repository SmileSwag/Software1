def gallons_to_liters(g):
    litres=g*3.785
    print(f"{g:.1f} American gallons is {litres:.2f} liters.")
    return
gallons=float(input("Enter a volume in American gallons (negative value to quit): "))
while gallons>=0:
    gallons_to_liters(gallons)
    gallons=float(input("Enter a volume in American gallons (negative value to quit): "))    
    
print("Program finished.")
    