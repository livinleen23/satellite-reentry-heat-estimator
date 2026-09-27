
import math

print("-------SATELLITE RE-ENTRY HEAT ESTIMATOR-------")

#inputs
Re_entry_Velocity=float(input("Re-entry velocity of the satellite(m/s):"))
Mass_of_the_satellite=float(input("weight of the satellite(Kg):"))
Surface_area=float(input("Surface area of the satellite(m^2):"))
Dynamic_pressure=float(input("Dynamic pressure(Pa):"))
Altitude=float(input("Satellite altitude(m):"))
Drag_coefficient=float(input("Drag coefficient:"))

#conditions
if Re_entry_Velocity<0:
    print("error:Re entry velocity can't be negative")
    exit()

if Mass_of_the_satellite<0:
    print("error:Mass of the satellite can't be negative ")
    exit()

if Surface_area<0:
    print("error:Surface area can't be negative")
    exit()

if Altitude<0:
    print("error:Altitude can't be negative")
    exit()

if Altitude >11000:
    print("error:this is a simplified model so inaccurate above 11000m")
    print("Altitude automatically set to 11000m")
    Altitude=11000

#values
T0=288.15     #sea level temperature in Kelvin(K)
P0=101325     #sea level pressure in Pascal(Pa)
R=287.05      #Specific gas constant(J/Kg K)
g=9.81        #Acceleration due to gravity(m/s^2)
L=0.0065      #Temperature lapse rate(K/m)
K=1*10**(-8)  #Simpliefied constant

#calculations
Atmospheric_temperature=T0-(L*Altitude)   #Atmospheric temperature
Atmospheric_pressure=P0*(Atmospheric_temperature/T0)**(g/(R*L))  #Atmospheric Pressure
Atmospheric_density=(Atmospheric_pressure/R*Atmospheric_temperature)  #Atmoshperic density
if Atmospheric_density <0:
   atmosperic_density=0.0    #Atmospheric density can't be negative
Drag_force=0.5*(Atmospheric_density*Drag_coefficient*Surface_area*(Re_entry_Velocity**2))   #Drag force in Newton(N)
Kinetic_energy=0.5*(Mass_of_the_satellite*(Re_entry_Velocity**2))   #Kinetic Energy in Joule(J)
Heat_flux=K*math.sqrt(Atmospheric_density)*(Re_entry_Velocity**3)   #Heat flux in Watts per metre square(W/m^2)
 

#Estimation

score=0

if Heat_flux>12000:
    score+=3                  #High risk
elif Heat_flux>6000:
    score+=2                  #Moderate risk
else :
    score+=1                  #Low risk

if Atmospheric_density<0.001:
    score+=1                     #Low risk
elif Atmospheric_density<0.01:
    score+=2                     #Moderat risk
else:
    score+=3                     #High risk

if Re_entry_Velocity>8000:
    score+=3                     #High risk
elif Re_entry_Velocity>5000:
    score+=2                     #Moderate risk
else:
    score+=1                     #Low risk

if Drag_force>1000000:
    score+=3                    #Highr risk
elif Drag_force>100000:
    score+=2                    #MOderate risk
else:
    score+=1                    #Low risk

#Risk Estimation

if score>9:
    Risk="HIGH"
elif score>5:
    Risk="MODERATE"
else:
    Risk="LOW"

#result
print("-------RESULTS-------")

print("Atmospheric Temperature: ", round(Atmospheric_temperature,2),"K")
print("Atmospheric Pressure: ", round(Atmospheric_pressure,2),"Pa")
print("Atmospheric Density: ", round(Atmospheric_density,3),"Kg/m^3")
print("Drag Force: ", round(Drag_force,2), round(Drag_force,2),"N")
print("Kinetic Energy: ", round(Kinetic_energy,2),"J")
print("Heat Flux: ", round(Heat_flux,2),"W/m^2")
print("Estimated Score:",score)
print("Risk Level:",Risk)

    
