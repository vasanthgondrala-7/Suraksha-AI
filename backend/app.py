from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ✅ Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # you can restrict later to ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Suraksha AI Backend is running"}

@app.get("/alerts")
def get_alerts():
    # Dummy alerts for testing
    return [
        {"id": 1, "type": "Weather", "message": "Heavy rainfall warning in Himachal Pradesh"},
        {"id": 2, "type": "Travel", "message": "Landslide reported near Manali-Leh highway"},
        {"id": 3, "type": "Health", "message": "Heatwave alert in Telangana"},
    ]
