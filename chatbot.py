import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")


def recommend_trials(patient, trials):

    patient_text = str(patient["DESCRIPTION"])

    trial_texts = trials["condition"].astype(str).tolist()

    patient_vec = model.encode([patient_text])
    trial_vecs = model.encode(trial_texts)

    sims = cosine_similarity(patient_vec, trial_vecs)[0]

    results = []

    for i in range(len(trials)):

        trial = trials.iloc[i]

        score = float(sims[i])

        results.append({
            "trial": trial["brief_title"],
            "score": score
        })

    results = sorted(results, key=lambda x: x["score"], reverse=True)

    return results[:10]