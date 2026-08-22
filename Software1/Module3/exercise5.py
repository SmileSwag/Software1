talents=float(input("Enter talents: "))
pounds=float(input("Enter pounds: "))
lots=float(input("Enter lots: "))
total_grams=(float(talents) * 20 * 32 + float(pounds) * 32 + float(lots)) * 13.3
kilograms=int(total_grams)//1000
remaining_grams=float(total_grams)%1000
print(f"The weight in modern units:\n{kilograms:.0f} kilograms and {remaining_grams:.2f} grams.")
