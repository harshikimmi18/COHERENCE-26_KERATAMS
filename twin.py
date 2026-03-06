import pandas as pd
from datetime import datetime


class DigitalTwin:

    def __init__(self, patient_row):
        self.patient = patient_row

    def calculate_age(self, birthdate):
        birth = datetime.strptime(birthdate, "%Y-%m-%d")
        today = datetime.today()
        return today.year - birth.year

    def profile(self):

        birthdate = str(self.patient["BIRTHDATE"])
        gender = self.patient["GENDER"]

        age = self.calculate_age(birthdate)

        return {
            "patient_id": self.patient["Id"],
            "age": age,
            "gender": gender
        }