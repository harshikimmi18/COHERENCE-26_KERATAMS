import pandas as pd

class DigitalTwin:

    def __init__(self, patient_row):

        self.patient_id = patient_row["Id"]
        self.age = int(patient_row["AGE"])
        self.gender = patient_row["GENDER"]
        self.conditions = patient_row["DESCRIPTION"]

    def profile(self):

        return {
            "patient_id": self.patient_id,
            "age": self.age,
            "gender": self.gender,
            "conditions": self.conditions
        }