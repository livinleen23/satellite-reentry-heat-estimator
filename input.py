def get_inputs():
    print("------SATELLITE RE-ENTRY HEAT ESTIMATOR-----")

    Re_entry_Velocity = float(input("Re_entry velocity of the satellite (m/s): ")) 
    Mass_of_the_satellite = float(input("Weight of the satellite (Kg):" ))
    Surface_area = float(input("Surface area of the satellite (m^2): "))
    Dynamic_pressure = float(input("Dynamic pressure (Pa): "))
    Altitude = float(input("Satellite altitude (m): "))
    Drag_coefficient = float(input("Drag coefficient: "))
    return (Re_entry_Velocity, Mass_of_the_satellite, Surface_area,Dynamic_pressure, Altitude, Drag_coefficient)