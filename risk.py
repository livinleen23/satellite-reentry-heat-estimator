def calculate_score(Heat_flux, Atmospheric_density, Re_entry_Velocity, Drag_force):

    score = 0

    if Heat_flux > 12000:
        score += 3
    elif Heat_flux > 6000:
        score += 2
    else:
        score += 1

    if Atmospheric_density < 0.1:
        score += 1
    elif Atmospheric_density < 0.5:
        score += 2
    else:
        score += 3

    if Re_entry_Velocity > 8000:
        score += 3
    elif Re_entry_Velocity > 5000:
        score += 2
    else:
        score += 1

    if Drag_force > 1000000:
        score += 3
    elif Drag_force > 100000:
        score += 2
    else:
        score +=1

    return score

def estimate_risk(score):

    if score > 9:
        return "HIGH"
    elif score > 5:
        return "MODERATE"
    else:
        return "LOW"
