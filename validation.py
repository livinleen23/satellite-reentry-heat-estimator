def validate_inputs(Re_entry_Velocity, Mass_of_the_satellite, Surface_area, Altitude):
    if Re_entry_Velocity < 0:
        print("Error: Re-entry velocity can't be negative")
        return False

    if Mass_of_the_satellite < 0:
        print("Error: Mass of the satellite can't be negative")
        return False

    if Surface_area < 0:
        print("Error: Surface area can't be negative")
        return False

    if Altitude < 0:
        print("Error: Altitude can't be negative")
        return False

    return True

def limit_altitude(Altitude):

    if Altitude > 11000:
        print("Error: This is a simplified model so inaccurate above 11000m")
        print("Altitude automatically set to 11000m")
        Altitude = 11000

    return Altitude