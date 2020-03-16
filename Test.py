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
    vehicle = input("Input car make, model, vehicle type, and year(Example: Ford Taurus 2018)\n")

    # Create list from user input
    vehicleInfo = vehicle.split()
    vehicleAge = currentYear - vehicleInfo[2]
    # Output information
    print("Manufacturer: ",vehicleInfo[0])
    print("Model: ",vehicleInfo[1])
    print("Age: ",vehicleAge)