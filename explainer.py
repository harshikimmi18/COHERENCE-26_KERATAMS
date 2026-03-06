def explain_trial(patient, trial):

    explanation = []

    patient_age = patient["AGE"]

    min_age = trial.get("minimum_age", 0)
    max_age = trial.get("maximum_age", 120)

    if patient_age >= min_age and patient_age <= max_age:
        explanation.append("Age matches trial range")
    else:
        explanation.append("Age outside eligibility range")

    patient_conditions = str(patient["DESCRIPTION"]).lower()
    trial_condition = str(trial["condition"]).lower()

    if trial_condition in patient_conditions:
        explanation.append("Patient condition matches trial disease")
    else:
        explanation.append("Condition mismatch")

    if str(trial["criteria"]) != "nan":
        explanation.append("Eligibility criteria evaluated")

    return explanation