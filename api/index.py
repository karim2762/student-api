from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
import json
import pathlib
from mangum import Mangum

app = FastAPI(title="Student Search API", version="2.0")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Load JSON — path relative to this file so Vercel can find it
DATA_PATH = pathlib.Path(__file__).parent.parent / "students.json"
with open(DATA_PATH, "r", encoding="utf-8") as f:
    students = json.load(f)

@app.get("/api/student/{roll_number}")
def get_student(roll_number: str):
    roll = roll_number.strip().lower()
    if not roll:
        raise HTTPException(status_code=400, detail="Roll number cannot be empty")
    if roll in students:
        return students[roll]
    raise HTTPException(status_code=404, detail=f"No student found with roll number '{roll_number}'")

@app.get("/api/search")
def search_students(
    q: str = Query(..., min_length=1, description="Search by name, roll number, or place"),
    limit: int = Query(default=10, ge=1, le=50)
):
    q_lower = q.strip().lower()
    results = []
    for roll, s in students.items():
        if (
            q_lower in s.get("name", "").lower()
            or q_lower in roll
            or q_lower in s.get("place", "").lower()
        ):
            results.append(s)
        if len(results) >= limit:
            break
    return {"count": len(results), "results": results}

@app.get("/api/stats")
def get_stats():
    total = len(students)
    genders = {}
    categories = {}
    for s in students.values():
        g = s.get("gender", "Unknown")
        genders[g] = genders.get(g, 0) + 1
        c = s.get("reservation_category", "Unknown") or "Unknown"
        categories[c] = categories.get(c, 0) + 1
    return {
        "total_students": total,
        "gender_distribution": genders,
        "category_distribution": categories,
    }

# Vercel serverless handler
handler = Mangum(app)
