ZanderLength=float(input("Enter the length of the zander in centimeters: "))
missing_cm= 42-ZanderLength
if ZanderLength >=42 :
    print("The zander meets the size limit.")

else :
    print("The zander does not meet the size limit.")
    print("Please release the fish back into the lake.")
    print(f"The fish was " + str(missing_cm:.1f) + " centimeters below the size limit.")