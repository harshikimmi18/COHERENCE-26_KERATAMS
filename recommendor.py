from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


def recommend_trials(patient, trials):

    # convert patient conditions to text
    patient_text = str(patient["DESCRIPTION"])

    # convert trial conditions to text list
    trial_conditions = trials["condition"].astype(str).tolist()

    # create embeddings
    patient_vec = model.encode([patient_text])
    trial_vecs = model.encode(trial_conditions)

    # calculate similarity
    scores = cosine_similarity(patient_vec, trial_vecs)[0]

    results = []

    for i in range(len(trials)):
        trial = trials.iloc[i]

        results.append({
            "trial": trial["brief_title"],
            "score": float(scores[i])
        })

    # sort best matches
    results = sorted(results, key=lambda x: x["score"], reverse=True)

    return results[:10]