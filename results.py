def display_results(Atmospheric_temperature, Atmospheric_pressure, Atmospheric_density, Drag_force, Kinetic_energy, Heat_flux, score, Risk):
    print("--------RESULTS--------")
    print("Atmospheric Temperature:", round(Atmospheric_temperature, 2), "K")
    print("Atmospheric Pressure:", round(Atmospheric_pressure, 2), "Pa")
    print("Atmospheric Density:", round(Atmospheric_density, 3), "Kg/m^3")
    print("Drag Force:", round(Drag_force, 2), "N")
    print("Kinetic Energy:", round(Kinetic_energy, 2), "J")
    print("Estimated Score:", score)
    print("Risk Level:", Risk)