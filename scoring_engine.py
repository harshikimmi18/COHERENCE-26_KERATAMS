def calculate_score(patient, trial):

    score = 0

    patient_conditions = [
        c.lower() for c in patient.get("conditions", [])
    ]

    trial_conditions = [
        c.lower() for c in trial.get("conditions", [])
    ]

    # Disease match
    matches = set(patient_conditions).intersection(
        set(trial_conditions)
    )

    if matches:
        score += 50

    # Age factor
    age = patient.get("age", 0)

    if 18 <= age <= 65:
        score += 20

    # Phase importance
    phase = str(trial.get("phase", "")).lower()

    if "phase 3" in phase:
        score += 20
    elif "phase 2" in phase:
        score += 10

    # Interventional trials bonus
    study_type = str(trial.get("study_type", "")).lower()

    if "interventional" in study_type:
        score += 10

    return min(score, 100)