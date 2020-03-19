# %%a
# %%a
# %%a
# %%a
# %%a
# %%a
# %%a
# %%a
# %%a
# %%a
# %%a
# %%a
# %%a
# %%a
# %%a
# %%a
# %%a
# %%a
# %%a
# %%a
# %%a
# %%a
# %%a
# %%a
# %%a
# %%a
# %%a
# %%a
# %%a
# %%a
# %%a
# %%a
# %%a
# %%a
# %%a
# %%a
# %%a
# %%a
# %%a
# %%a
# %%a
# %%a
# %%a
# %%a
# %%a
# %%a
# %%a
# %%a
# %%a
# %%a
# %%a
# %%a
# %%a
# %%a
# start
    currentYear = 2020
    # Get vehicle information from the user
    vehicle = input("Input car make, model, color, year, and vehicle type(Example: Ford Taurus 2018 Car)\n")

    # Create list from user input
    vehicleInfo = vehicle.split()
    vehicleAge = currentYear - vehicleInfo[3]

    # Output information
    print("Manufacturer: ",vehicleInfo[0])
    print("Model: ",vehicleInfo[1])
    print("Color: ",vehicleInfo[2])
    print("Year: ",vehicleInfo[3])
    print("Vehicle Type: ",vehicleInfo[4])
    print("Age: ",vehicleAge)