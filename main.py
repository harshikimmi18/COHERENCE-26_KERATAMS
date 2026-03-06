from fastapi import FastAPI
import pandas as pd
import os

from app.twin import DigitalTwin
from app.recommendor import recommend_trials


app = FastAPI(title="AI Clinical Trial Twin System")


# -----------------------------
# DATA PATHS
# -----------------------------

PATIENT_DATA_PATH = "data/synthea_sample_data_csv_latest"
TRIAL_DATA_PATH = "data/1ycgnmbywtf11570j6bz081gova6"


# -----------------------------
# LOAD PATIENT DATA (Synthea)
# -----------------------------

patients = pd.read_csv(os.path.join(PATIENT_DATA_PATH, "patients.csv"))
conditions = pd.read_csv(os.path.join(PATIENT_DATA_PATH, "conditions.csv"))


# -----------------------------
# LOAD TRIAL DATA (Clinical Trials)
# -----------------------------

studies = pd.read_csv(os.path.join(TRIAL_DATA_PATH, "studies.txt"), sep="|", low_memory=False)
trial_conditions = pd.read_csv(os.path.join(TRIAL_DATA_PATH, "conditions.txt"), sep="|", low_memory=False)
eligibilities = pd.read_csv(os.path.join(TRIAL_DATA_PATH, "eligibilities.txt"), sep="|", low_memory=False)


# Merge trial data
trials = studies.merge(trial_conditions, on="nct_id", how="left")

trials = trials.merge(
    eligibilities[["nct_id", "criteria", "minimum_age", "maximum_age"]],
    on="nct_id",
    how="left"
)


trials = trials[[
    "nct_id",
    "brief_title",
    "name",
    "criteria",
    "minimum_age",
    "maximum_age"
]].rename(columns={"name": "condition"})


# -----------------------------
# ROOT
# -----------------------------

@app.get("/")
def home():

    return {
        "message": "AI Clinical Trial Twin API Running"
    }


# -----------------------------
# DIGITAL TWIN
# -----------------------------

@app.get("/twin/{patient_id}")
def get_twin(patient_id: int):

    patient = patients.iloc[patient_id]

    twin = DigitalTwin(patient)

    profile = twin.profile()

    patient_conditions = conditions[
        conditions["PATIENT"] == patient["Id"]
    ]["DESCRIPTION"].tolist()

    profile["conditions"] = patient_conditions

    return profile


# -----------------------------
# TRIAL RECOMMENDATION
# -----------------------------

@app.get("/recommend/{patient_id}")
def recommend(patient_id: int):

    patient = patients.iloc[patient_id]

    patient_conditions = conditions[
        conditions["PATIENT"] == patient["Id"]
    ]["DESCRIPTION"].tolist()

    patient_text = " ".join(patient_conditions)

    patient_data = {
        "DESCRIPTION": patient_text
    }

    results = recommend_trials(patient_data, trials)

    return {
        "recommended_trials": results
    }