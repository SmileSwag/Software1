airports = {}

while True:
    print("\nAirport Data Management")
    print("1. Enter a new airport")
    print("2. Fetch airport information")
    print("3. Quit")
    
    choice = input("Please choose an option (1-3): ")
    
    if choice == "1":
        icao_code = input("Enter the ICAO code: ")
        airport_name = input("Enter the airport name: ")
        airports[icao_code] = airport_name
        print(f"Airport {airport_name} with ICAO code {icao_code} has been added.")
    
    elif choice == "2":
        icao_code = input("Enter the ICAO code: ")
        if icao_code in airports:
            print(f"The airport with ICAO code {icao_code} is {airports[icao_code]}.")
        else:
            print(f"No airport found with ICAO code {icao_code}.")
    
    elif choice == "3":
        print("Thank you for using the Airport Data Management system. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")
