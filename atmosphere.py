T0 = 288.15
P0 = 101325
R = 287.05
g = 9.81
L = 0.0065


def calculate_atmosphere(Altitude):

    Atmospheric_temperature = T0 - (L * Altitude)

    Atmospheric_pressure = P0 * (Atmospheric_temperature / T0) ** (g / (R * L))

    Atmospheric_density = Atmospheric_pressure / (R * Atmospheric_temperature)

    if Atmospheric_density < 0:
        Atmospheric_density = 0.0

    return(Atmospheric_temperature, Atmospheric_pressure, Atmospheric_density)