
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI()

# Trained Decision Tree model load karein
model = joblib.load("model.pkl")

# Student ka input structure
class Student(BaseModel):
    Study_Hours: float
    Attendance: float

# Prediction API
@app.post("/predict")
def predict(student: Student):

    student_data = pd.DataFrame([{
        "Study_Hours": student.Study_Hours,
        "Attendance": student.Attendance
    }])

    prediction = model.predict(student_data)[0]

    return {
        "prediction": str(prediction)
    }

# Frontend website connect karein
app.mount(
    "/",
    StaticFiles(directory="static", html=True),
    name="static"
)
