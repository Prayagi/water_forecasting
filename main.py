from fastapi import FastAPI, Request
import pickle
import numpy as np
import os

app = FastAPI()

# -------------------------------
# Helper: safe model loading
# -------------------------------
def load_model(path):
    try:
        return pickle.load(open(path, "rb"))
    except Exception as e:
        print(f"Error loading model from {path}: {e}")
        return None

# -------------------------------
# Load your models (UPDATE PATHS)
# -------------------------------

# ⚠️ IMPORTANT: Fix folder names if needed (no spaces ideally)

water_model_path = "project Model/WaterDemandPrediction_Model/water_model.pkl"
sector_model_path = "project Model/SectorRiskPrediction_Model/sector_model.pkl"
capacity_model_path = "project Model/CapacityPrediction_Model/capacity_model.pkl"

water_model = load_model(water_model_path)
sector_model = load_model(sector_model_path)
capacity_model = load_model(capacity_model_path)

# -------------------------------
# Root route
# -------------------------------
@app.get("/")
def home():
    return {"status": "API running 🚀"}

# -------------------------------
# Water Prediction
# -------------------------------
@app.post("/predict_water")
async def predict_water(request: Request):
    data = await request.json()

    try:
        features = list(data.values())
        features = np.array(features).reshape(1, -1)

        prediction = water_model.predict(features)
        return {"prediction": float(prediction[0])}

    except Exception as e:
        return {"error": str(e)}

# -------------------------------
# Sector Risk Prediction
# -------------------------------
@app.post("/predict_sector")
async def predict_sector(request: Request):
    data = await request.json()

    try:
        features = list(data.values())
        features = np.array(features).reshape(1, -1)

        prediction = sector_model.predict(features)
        return {"prediction": float(prediction[0])}

    except Exception as e:
        return {"error": str(e)}

# -------------------------------
# Capacity Prediction
# -------------------------------
@app.post("/predict_capacity")
async def predict_capacity(request: Request):
    data = await request.json()

    try:
        features = list(data.values())
        features = np.array(features).reshape(1, -1)

        prediction = capacity_model.predict(features)
        return {"prediction": float(prediction[0])}

    except Exception as e:
        return {"error": str(e)}