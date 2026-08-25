gender=input("Enter biological gender (male/female): ")
hemoglobin=float(input("Enter hemoglobin value (g/l): "))
if gender == "male":
    if hemoglobin >134 and hemoglobin < 167:
        print("Your hemoglobin is normal.")
    elif hemoglobin <= 134:
        print("Your hemoglobin is low.")
    elif hemoglobin >=167:
        print("Your hemoglobin is high.")
if gender == "female":
    if hemoglobin >117 and hemoglobin < 155:
        print("Your hemoglobin is normal.")
    elif hemoglobin <= 117:
        print("Your hemoglobin is low.")
    elif hemoglobin >=155:
        print("Your hemoglobin is high.")