import random

conditions_pool = [
    "diabetes",
    "hypertension",
    "asthma",
    "depression",
    "heart disease",
    "arthritis",
    "copd",
    "stroke",
    "cancer"
]

genders = ["M", "F"]

def generate_twin():

    twin = {
        "age": random.randint(18, 80),
        "gender": random.choice(genders),
        "conditions": random.sample(conditions_pool, random.randint(1,3))
    }

    return twin