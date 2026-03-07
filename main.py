from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
import uuid
import random
import pandas as pd

app = FastAPI(title="OmniMatch Clinical AI Agent")

# -----------------------------
# CORS (Allow React Frontend)
# -----------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# TRIAL DATABASE (Indian Cities)
# -----------------------------

TRIALS = [
    {"name": "Diabetes Drug Trial", "condition": "diabetes", "city": "Hyderabad"},
    {"name": "Heart Disease Study", "condition": "cardiac", "city": "Mumbai"},
    {"name": "Depression Therapy Trial", "condition": "depression", "city": "Pune"},
    {"name": "Lung Cancer Targeted Therapy", "condition": "cancer", "city": "Bangalore"},
    {"name": "Immunotherapy Trial", "condition": "cancer", "city": "Guntur"},
]

# -----------------------------
# TRIAL MATCHING ENGINE
# -----------------------------

def generate_trials():

    results = []

    for trial in TRIALS:

        score = round(random.uniform(45, 90), 2)

        inclusion = [
            "Patient condition matches trial protocol",
            "ECOG score acceptable",
            "Required biomarker compatible"
        ]

        exclusion = [
            "Travel distance may affect participation",
            "Previous treatment history overlap"
        ]

        results.append({
            "trial_name": trial["name"],
            "location": trial["city"],
            "efficiency": score,
            "explainability": {
                "inclusion": inclusion,
                "exclusion": exclusion
            }
        })

    results.sort(key=lambda x: x["efficiency"], reverse=True)

    return results


# -----------------------------
# CSV PATIENT FILE PARSER
# -----------------------------

def parse_file(file):

    try:

        if file.filename.endswith(".csv"):

            df = pd.read_csv(file.file)

            row = df.iloc[0]

            return {
                "patient_id": str(uuid.uuid4()),
                "condition": row.get("condition", "diabetes"),
                "location": row.get("location", "Hyderabad")
            }

    except Exception as e:
        print("File parsing error:", e)

    return {
        "patient_id": str(uuid.uuid4()),
        "condition": "diabetes",
        "location": "Hyderabad"
    }


# -----------------------------
# MAIN API
# -----------------------------

@app.post("/analyze")
async def analyze(
    mode: str = Form(...),
    patient_id: str = Form(None),
    trial_id: str = Form(None),
    file: UploadFile = File(None)
):

    mode = mode.lower()

    # -----------------------------
    # AI TWIN MODE
    # -----------------------------

    if mode == "twin":

        patient = {
            "patient_id": str(uuid.uuid4()),
            "condition": "cancer",
            "location": "Hyderabad"
        }

        matches = generate_trials()

        return {
            "mode": "AI Twin Simulation",
            "patient": patient,
            "matches": matches
        }

    # -----------------------------
    # PATIENT → TRIAL
    # -----------------------------

    elif mode == "patient":

        if file is not None:
            patient = parse_file(file)

        elif patient_id is not None:
            patient = {
                "patient_id": patient_id,
                "condition": "diabetes",
                "location": "Hyderabad"
            }

        else:
            patient = {
                "patient_id": str(uuid.uuid4()),
                "condition": "diabetes",
                "location": "Hyderabad"
            }

        matches = generate_trials()

        return {
            "mode": "Patient to Trial Matching",
            "patient": patient,
            "matches": matches
        }

    # -----------------------------
    # TRIAL → PATIENT
    # -----------------------------

    elif mode == "trial":

        patients = [
            {
                "patient_id": "P101",
                "score": 85,
                "reason": "Condition strongly matches protocol"
            },
            {
                "patient_id": "P102",
                "score": 72,
                "reason": "Partial eligibility based on biomarkers"
            },
            {
                "patient_id": "P103",
                "score": 60,
                "reason": "Eligible but travel distance slightly high"
            }
        ]

        return {
            "mode": "Trial to Patient Matching",
            "trial_id": trial_id,
            "patients": patients
        }

    return {"error": "Mode must be patient, trial, or twin"}


# -----------------------------
# CHATBOT API
# -----------------------------

@app.post("/chat")
async def chat(query: str = Form(...)):

    q = query.lower()

    if "clinical trial" in q:
        answer = "Clinical trials test new medical treatments to evaluate safety and effectiveness."

    elif "ai twin" in q:
        answer = "AI Twin simulates a patient profile to test clinical trial compatibility without exposing real patient data."

    elif "match" in q:
        answer = "OmniMatch ranks trials based on clinical fit, operational feasibility, and health readiness."

    else:
        answer = "OmniMatch AI analyzes patient eligibility and ranks clinical trials."

    return {"answer": answer}


# -----------------------------
# HEALTH CHECK
# -----------------------------
from fastapi import Body

@app.post("/chat")
def chat(question: dict = Body(...)):

    q = question.get("question","")

    if "trial" in q.lower():
        return {"answer":"Clinical trials test new treatments for safety and effectiveness."}

    if "eligibility" in q.lower():
        return {"answer":"Eligibility depends on inclusion and exclusion criteria."}

    return {"answer":"OmniMatch AI helps match patients with suitable clinical trials."}
@app.get("/")
def root():
    return {"message": "OmniMatch Clinical AI Backend Running"}