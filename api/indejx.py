from fastapi import FastAPI, HTTPException
import json

app = FastAPI(title="Student Search API")

# Load JSON once when the server starts
with open("students.json", "r", encoding="utf-8") as f:
    students = json.load(f)

@app.get("/")
def home():
    return {"message": "Student API Running"}

@app.get("/student/{roll_number}")
def get_student(roll_number: str):
    roll = roll_number.lower()

    if roll in students:
        return students[roll]

    raise HTTPException(status_code=404, detail="Student not found")
