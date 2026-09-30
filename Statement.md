# Project Statement

## Project Title

**Satellite Re-Entry Heat Estimator**

---

## 1. Problem Statement

During atmospheric re-entry, a satellite travels through Earth's atmosphere at very high velocity and experiences aerodynamic forces and heating. Understanding the relationship between re-entry velocity, atmospheric conditions, and aerodynamic heating is an important basic concept in aerospace engineering.

However, actual spacecraft re-entry analysis involves complex physics and advanced computational models. For a beginner-level aerospace and Python project, there is a need for a simple computational tool that can accept basic satellite re-entry parameters and provide an educational estimate of atmospheric conditions, drag force, kinetic energy, heat flux, and an associated heat/risk level.

The **Satellite Re-Entry Heat Estimator** addresses this problem by providing a modular Python program that uses simplified atmospheric and aerodynamic equations to process user-provided re-entry parameters and present the calculated results in a clear format.

This project is intended for **educational and academic purposes** and is not a replacement for detailed spacecraft re-entry analysis.

---

## 2. Scope of the Project

The project focuses on developing a command-line Python application for a simplified study of satellite atmospheric re-entry.

The system accepts the following user inputs:

- Re-entry velocity
- Satellite mass
- Satellite surface area
- Dynamic pressure
- Satellite altitude
- Drag coefficient

The program then:

1. Validates selected input values.
2. Limits the altitude to the range supported by the simplified atmospheric model.
3. Estimates atmospheric temperature.
4. Estimates atmospheric pressure.
5. Calculates atmospheric density.
6. Calculates aerodynamic drag force.
7. Calculates satellite kinetic energy.
8. Calculates an estimated heat flux.
9. Calculates a simplified numerical score.
10. Converts the score into a LOW, MODERATE, or HIGH risk level.
11. Displays the calculated results to the user.

The project does **not** attempt to model a complete real-world spacecraft re-entry. It does not include detailed computational fluid dynamics, complete re-entry trajectory simulation, thermal protection system modelling, or advanced atmospheric models.

---

## 3. Target Users

The intended users of this project are:

- Aerospace Engineering students
- Students learning Python programming
- Beginners studying atmospheric re-entry concepts
- Students working on introductory aerospace simulation projects
- Learners interested in applying programming to engineering problems

The project is particularly suitable for students who want to understand how basic Python programming can be combined with aerospace engineering calculations.

---

## 4. High-Level Features

### 4.1 User Input Module

The program collects the satellite's re-entry parameters from the user, including velocity, mass, surface area, dynamic pressure, altitude, and drag coefficient.

### 4.2 Input Validation

The program checks whether velocity, mass, surface area, and altitude are negative. Invalid values are rejected and an error message is displayed.

### 4.3 Atmospheric Calculation

The program estimates atmospheric temperature, pressure, and density using a simplified atmospheric model.

### 4.4 Aerodynamic Calculations

The program calculates:

- Drag force
- Kinetic energy
- Estimated heat flux

### 4.5 Risk/Heat-Level Estimation

The program assigns a numerical score using heat flux, atmospheric density, velocity, and drag force. The score is then converted into one of three levels:

- **LOW**
- **MODERATE**
- **HIGH**

### 4.6 Result Display

The calculated atmospheric and aerodynamic values, score, and risk level are displayed to the user in a structured output.

---

## 5. Project Objective

The overall objective is to develop a simple and modular Python-based educational tool that demonstrates how basic aerospace parameters can be processed to estimate atmospheric conditions, aerodynamic effects, and re-entry heating.

The project aims to connect theoretical aerospace concepts with practical Python implementation while maintaining a clear, beginner-friendly structure.

---

