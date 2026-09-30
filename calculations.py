import math

K = 1 * 10**(-8)

def calculate_drag_force(Atmospheric_density, Drag_coefficient, Surface_area, Re_entry_Velocity):

    Drag_force = 0.5 * (Atmospheric_density * Drag_coefficient * Surface_area * (Re_entry_Velocity ** 2))
    return Drag_force


def calculate_kinetic_energy(Mass_of_the_satellite, Re_entry_Velocity):

    Kinetic_energy = 0.5 * (Mass_of_the_satellite * (Re_entry_Velocity ** 2))
    return Kinetic_energy

def calculate_heat_flux(Atmospheric_density, Re_entry_Velocity):

    Heat_flux = (K * math.sqrt(Atmospheric_density) * (Re_entry_Velocity **3))
    return Heat_flux