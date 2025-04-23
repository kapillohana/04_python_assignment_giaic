# Define the speed of light as a constant (in meters per second)
C = 299792458 
def main():
    mass_in_kg = float(input("Enter killos of mass: "))

    # Calculate the equivalent energy using Einstein's mass-energy equivalence formula:
    # E = m * c^2
    # Where:
    #   E = energy in joules
    #   m = mass in kilograms
    #   c = speed of light (299792458 m/s)
    energy_in_jouls = mass_in_kg * (C ** 2)

    # Print the mass value that was input
    print ("e = m * C^2...")

    # Print the speed of light constant
    print("C = " + str(C) + " m/s")
    
    # Print the calculated energy in joules
    # Using scientific notation for very large numbers
    print(str(energy_in_jouls) + " joules of energy!")


# This standard Python idiom checks if the script is being run directly
# (as opposed to being imported as a module)
if __name__ == '__main__':
    main()