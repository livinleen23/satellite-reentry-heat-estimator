#  Satellite Re-Entry Heat Estimator

A beginner-friendly Python project that provides a simplified estimate of aerodynamic heating experienced by a satellite during atmospheric re-entry.

---

##  Project Overview

The **Satellite Re-Entry Heat Estimator** is a Python-based program designed to estimate the heating experienced by a satellite during atmospheric re-entry.

When a satellite enters Earth's atmosphere at very high velocity, it interacts with atmospheric particles and experiences significant aerodynamic heating. This project uses basic aerospace engineering concepts and Python programming to provide a simplified estimation of this heating.

> **Note:** This is an educational model and does not represent the complete physics of an actual spacecraft re-entry.

---

##  Objectives

The main objectives of this project are:

- Understand the heating experienced during atmospheric re-entry
- Apply basic aerospace engineering concepts using Python
- Calculate an estimated heating value using user inputs
- Understand the relationship between velocity, altitude, atmospheric density, and heating
- Develop a simple and user-friendly Python program
- Practice Python programming concepts such as functions, variables, conditions, and mathematical calculations

---

##  Features

-  Accepts satellite re-entry parameters from the user
-  Estimates aerodynamic heating
-  Uses basic mathematical equations
-  Provides a simple heat/risk-level indication
-  Runs directly in Python
-  Beginner-friendly code structure
-  Can be expanded into a more advanced aerospace simulation

---

##  Parameters Used

| Parameter | Description | Unit |
|---|---|---|
| Velocity | Speed of the satellite during re-entry | m/s |
| Altitude | Height above Earth's surface | m / km |
| Air Density | Density of atmospheric air | kg/m³ |
| Heating Value | Estimated aerodynamic heating | Model-dependent |

---

##  Basic Principle

During atmospheric re-entry, a satellite travels through the atmosphere at extremely high velocity.

A simplified relationship for aerodynamic heating can be represented as:

### **Heating ∝ ρV³**

Where:

- **ρ** = Atmospheric density
- **V** = Re-entry velocity

This relationship shows that velocity has a strong effect on aerodynamic heating. Since velocity is raised to the third power, even a change in velocity can significantly affect the estimated heating.

Actual spacecraft re-entry heating is much more complex and depends on several factors, including:

- Atmospheric density
- Re-entry velocity
- Spacecraft shape
- Re-entry trajectory
- Drag coefficient
- Surface material and properties
- Atmospheric temperature and composition

Therefore, this project is intended primarily as an **educational estimator** rather than a real spacecraft design or flight-analysis tool.

---

##  Calculation Model

The program uses simplified aerospace equations to estimate important quantities related to re-entry.

### Atmospheric Temperature

A simplified atmospheric model is used to estimate temperature based on altitude.

### Atmospheric Pressure

Atmospheric pressure is estimated using the simplified atmospheric model.

### Atmospheric Density

Density is calculated using:

```text
ρ = P / RT
```

Where:

- `ρ` = Atmospheric density
- `P` = Atmospheric pressure
- `R` = Specific gas constant for air
- `T` = Atmospheric temperature

### Drag Force

The simplified aerodynamic drag equation is:

```text
F_D = 1/2 ρ C_D A V²
```

Where:

- `F_D` = Drag force
- `ρ` = Atmospheric density
- `C_D` = Drag coefficient
- `A` = Surface area
- `V` = Velocity

### Kinetic Energy

The satellite's kinetic energy is calculated using:

```text
KE = 1/2 mV²
```

Where:

- `m` = Mass of satellite
- `V` = Re-entry velocity

### Heat Flux

A simplified heating relationship is used:

```text
q ∝ √ρ V³
```

This provides an educational estimate of the aerodynamic heating during re-entry.

---

## 🛠️ Technologies Used

- **Python 3**
- Variables
- User input and output
- Mathematical calculations
- Functions
- Conditional statements
- Modular programming
- Basic aerospace engineering concepts

---

##  Project Structure

The project is divided into multiple Python modules:

```text
satellite-reentry-heat-estimator/
│
├── main.py
├── inputs.py
├── validation.py
├── atmosphere.py
├── calculations.py
├── risk.py
├── results.py
└── README.md
```

### Module Description

| File | Purpose |
|---|---|
| `main.py` | Controls and runs the complete program |
| `inputs.py` | Collects user inputs |
| `validation.py` | Validates input values |
| `atmosphere.py` | Calculates atmospheric properties |
| `calculations.py` | Performs drag, kinetic energy, and heating calculations |
| `risk.py` | Calculates the simplified heat/risk score |
| `results.py` | Displays the final results |
| `README.md` | Project documentation |

---

##  How to Run

### Step 1 — Install Python

Download and install **Python 3** on your computer.

You can check whether Python is installed by running:

```bash
python --version
```

---

### Step 2 — Clone the Repository

Clone this repository using Git:

```bash
git clone https://github.com/your-username/satellite-reentry-heat-estimator.git
```

Then move into the project directory:

```bash
cd satellite-reentry-heat-estimator
```

---

### Step 3 — Run the Program

Run:

```bash
python main.py
```

The program will ask you to enter the required satellite re-entry parameters.

Example:

```text
-------SATELLITE RE-ENTRY HEAT ESTIMATOR-------

Re-entry velocity of the satellite (m/s):
Weight of the satellite (Kg):
Surface area of the satellite (m^2):
Dynamic pressure (Pa):
Satellite altitude (m):
Drag coefficient:
```

The program will then calculate the atmospheric conditions, drag force, kinetic energy, estimated heat flux, and simplified risk level.

---

##  Example Output

```text
-------RESULTS-------

Atmospheric Temperature: 216.65 K
Atmospheric Pressure: 22632.06 Pa
Atmospheric Density: 0.364 kg/m³

Drag Force: 123456.78 N
Kinetic Energy: 2500000000.00 J
Heat Flux: 9876.54 W/m²

Estimated Score: 8
Risk Level: MODERATE
```

> The values above are only example values. Actual results depend on the inputs provided by the user.

---

##  Applications

This project can be used for:

- Understanding atmospheric re-entry
- Learning basic aerospace engineering concepts
- Practicing Python programming
- Understanding the effect of velocity on aerodynamic heating
- Exploring the relationship between altitude and atmospheric density
- Learning modular Python programming
- Developing a foundation for more advanced aerospace simulations

---

##  Future Improvements

The project can be further improved by adding:

- [ ] Mach number calculations
- [ ] Dynamic atmospheric density based on altitude
- [ ] More detailed temperature estimation
- [ ] More realistic heat-transfer calculations
- [ ] Different spacecraft shapes
- [ ] Re-entry trajectory simulation
- [ ] Graphs showing heating vs. altitude
- [ ] Graphs showing heating vs. velocity
- [ ] Graphical User Interface (GUI)
- [ ] Advanced atmospheric models
- [ ] CSV data logging
- [ ] Visualization of the re-entry profile
- [ ] Comparison of different spacecraft configurations

---

##  Limitations

This project uses a **simplified mathematical model** and should not be used for real spacecraft design, mission planning, or safety-critical calculations.

Real atmospheric re-entry analysis requires significantly more advanced models involving:

- Computational fluid dynamics
- High-temperature gas dynamics
- Atmospheric composition
- Shock-wave behaviour
- Convective and radiative heating
- Thermal protection systems
- Vehicle orientation and trajectory
- Time-dependent atmospheric conditions

The purpose of this project is to demonstrate the application of **basic aerospace concepts through Python programming**.

---

##  Author

**Livin Leen**

B.Tech Aerospace Engineering  
VIT Bhopal University

---

##  License

This project is intended for **educational and academic purposes**.

You are free to study and modify the code for learning and non-commercial academic use.
