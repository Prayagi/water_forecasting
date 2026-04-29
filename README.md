# 💧 Aqua Forecast - AI-Powered Water Resource Management System

> A full-stack web application that leverages Machine Learning to predict water demand, reservoir capacity, and sector-wise risk assessment - empowering sustainable water management decisions.

---

## 📋 Table of Contents

- [About the Project](#about-the-project)
- [Aim](#aim)
- [Objectives](#objectives)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [ML Models Overview](#ml-models-overview)
- [Prerequisites](#prerequisites)
- [Installation & Setup](#installation--setup)
- [Running the Application](#running-the-application)
- [Usage Guide](#usage-guide)
- [API Endpoints](#api-endpoints)
- [Screenshots](#screenshots)
- [Team](#team)
- [License](#license)

---

## 📖 About the Project

**Aqua Forecast** is a Minor Project that combines a modern web interface with multiple Machine Learning models to provide intelligent predictions related to water resource management. The system helps urban planners, water authorities, and researchers make data-driven decisions about water supply, reservoir management, and sector-level risk evaluation.

The application features a sleek ocean-themed UI with dynamic rain animations, glassmorphism design elements, and three core prediction modules , each powered by a dedicated ML model running as a separate Flask microservice.

---

## 🎯 Aim

To develop an AI-powered water resource management system that provides accurate predictions for water demand, reservoir capacity, and sector-wise risk assessment, enabling proactive and sustainable water management in urban areas.

---

## 📌 Objectives

1. **Water Demand Prediction** — Forecast water demand based on city, season, temperature, rainfall, population, reservoir level, water tariff, and historical demand patterns.
2. **Reservoir Capacity Prediction** — Predict the capacity percentage of a reservoir based on rainfall, inflow, outflow, and runoff factor.
3. **Sector-Wise Risk Assessment** — Assess the water supply risk level (Low / Medium / High) for a sector based on population, capacity, inflow, outflow, and reservoir level.
4. **User-Friendly Interface** — Provide an intuitive, visually appealing web interface for non-technical users to interact with the ML models.

---

## 🛠️ Tech Stack

### Frontend
| Technology | Purpose |
|---|---|
| **HTML5** | Page structure & semantic markup |
| **CSS3** | Styling, glassmorphism, animations |
| **JavaScript (Vanilla)** | Client-side logic, rain animations, API calls |
| **EJS** | Server-side templating for dynamic pages |
| **Google Fonts** | Cinzel & Raleway typography |

### Backend
| Technology | Purpose |
|---|---|
| **Node.js** | Web server runtime |
| **Express.js v5** | Web framework for routing & static file serving |
| **Flask** | Python microservices for ML model serving |
| **Flask-CORS** | Cross-Origin Resource Sharing for API communication |

### Machine Learning
| Technology | Purpose |
|---|---|
| **scikit-learn** | RandomForestRegressor models |
| **pandas** | Data manipulation & preprocessing |
| **joblib** | Model serialization (.pkl files) |
| **NumPy** | Numerical computations |

---

## 📁 Project Structure

```
Minor-project/
│
├── index.js                        # Express.js server (main entry point)
├── package.json                    # Node.js dependencies & scripts
├── README.md                       # This file
│
├── views/                          # EJS templates (server-rendered pages)
│   ├── in.ejs                      # Landing page template
│   └── menu.ejs                    # Menu/dashboard template
│
├── public/                         # Static assets served by Express
│   ├── HTML_File/
│   │   ├── index.html              # Landing page (static version)
│   │   ├── menu.html               # Menu page (static version)
│   │   ├── predict_water_demand.html    # Water demand prediction form
│   │   ├── predict_capacity.html        # Reservoir capacity prediction form
│   │   └── predict_sector_risk.html     # Sector risk assessment form
│   │
│   ├── CSS_File/
│   │   ├── in.css                  # Landing page styles
│   │   └── menu.css                # Menu page styles
│   │
│   └── JavaScript_File/
│       ├── in.js                   # Landing page scripts (rain animation)
│       └── menu.js                 # Menu page scripts (rain animation)
│
└── project Model/                  # ML models directory
    │
    ├── WaterDemandPrediction_Model/     # 🔹 Water Demand Model
    │   ├── app.py                       # Flask server (port 5000)
    │   ├── model.ipynb                  # Jupyter notebook (training)
    │   ├── water_model.pkl              # Trained model file
    │   ├── columns.pkl                  # Feature columns metadata
    │   ├── mp_water_demand_4000_rows.csv # Training dataset
    │   └── requirements.txt             # Python dependencies
    │
    ├── capacity_model/                  # 🔹 Reservoir Capacity Model
    │   ├── server.py                    # Flask server (port 5002)
    │   ├── capacity_model.pkl           # Trained model file
    │   └── reservoir_capacity_dataset.csv # Training dataset
    │
    └── sector_model/                    # 🔹 Sector Risk Assessment Model
        ├── server.py                    # Flask server (port 5001)
        ├── app.py                       # Model training script
        ├── app.ipynb                    # Jupyter notebook (training)
        ├── sector_model.pkl             # Trained model file
        └── newDataset_with_demand.csv   # Training dataset
```

---

## 🤖 ML Models Overview

### 1. Water Demand Prediction Model (`port 5000`)
- **Algorithm:** Random Forest Regressor
- **Input Features:** Temperature, Rainfall, Population, Reservoir Level, Water Tariff, Holiday flag, Previous Day Demand (lag_1), Last Week Demand (lag_7), City, Season
- **Output:** Predicted water demand (in units)
- **Endpoint:** `POST /predict`

### 2. Reservoir Capacity Prediction Model (`port 5002`)
- **Algorithm:** Random Forest Regressor (100 estimators)
- **Input Features:** Rainfall (mm), Inflow (cumecs), Outflow (cumecs), Runoff Factor
- **Output:** Predicted capacity percentage (0–100%)
- **Endpoint:** `POST /predict_capacity`

### 3. Sector-Wise Risk Assessment Model (`port 5001`)
- **Algorithm:** Random Forest Regressor (100 estimators)
- **Input Features:** Population, Capacity, Inflow, Outflow, Reservoir Level
- **Output:** Predicted water demand, Risk Level (Low/Medium/High), Risk Ratio
- **Risk Classification:**
  - `Risk Ratio > 0.8` → **High Risk** 🔴
  - `Risk Ratio > 0.5` → **Medium Risk** 🟠
  - `Risk Ratio ≤ 0.5` → **Low Risk** 🟢
- **Endpoint:** `POST /predict_risk`

---

## ✅ Prerequisites

Before running the project, ensure you have the following installed:

| Software | Version | Download Link |
|---|---|---|
| **Node.js** | v18+ recommended | [nodejs.org](https://nodejs.org/) |
| **Python** | 3.8+ | [python.org](https://www.python.org/) |
| **pip** | Latest | Comes with Python |
| **Git** | Latest | [git-scm.com](https://git-scm.com/) |

---

## 🚀 Installation & Setup

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd Minor-project
```

### Step 2: Install Node.js Dependencies

```bash
npm install
```

This installs the following packages:
- `express` — Web framework
- `ejs` — Templating engine

### Step 3: Install Python Dependencies

Install the required Python packages for **all three ML models**:

```bash
pip install flask flask-cors pandas scikit-learn joblib numpy
```

Or, using the provided requirements file:

```bash
pip install -r "project Model/WaterDemandPrediction_Model/requirements.txt"
```

> **Note:** The `sector_model/app.py` training script also uses `matplotlib` and `seaborn` for visualizations. Install them if you plan to retrain:
> ```bash
> pip install matplotlib seaborn
> ```

---

## ▶️ Running the Application

You need to start **4 servers** in separate terminals — 1 Node.js frontend server + 3 Flask ML backend servers.

### Terminal 1 — Start the Web Server (Node.js)

```bash
cd Minor-project
npm run dev
```

> This starts the Express server at **http://localhost:3000** with auto-restart on file changes.
>
> Alternatively, for production:
> ```bash
> npm start
> ```

### Terminal 2 — Start the Water Demand Model (Flask, Port 5000)

```bash
cd "project Model/WaterDemandPrediction_Model"
python app.py
```

> Starts at **http://127.0.0.1:5000**

### Terminal 3 — Start the Sector Risk Model (Flask, Port 5001)

```bash
cd "project Model/sector_model"
python server.py
```

> Starts at **http://127.0.0.1:5001**
>
> ⚠️ **Important:** Run `server.py` (not `app.py`). The `app.py` file is the training script, not the API server.

### Terminal 4 — Start the Capacity Model (Flask, Port 5002)

```bash
cd "project Model/capacity_model"
python server.py
```

> Starts at **http://127.0.0.1:5002**

### Quick Start (All-in-One Summary)

| Terminal | Command | Directory | Port |
|---|---|---|---|
| 1 | `npm run dev` | `Minor-project/` | 3000 |
| 2 | `python app.py` | `project Model/WaterDemandPrediction_Model/` | 5000 |
| 3 | `python server.py` | `project Model/sector_model/` | 5001 |
| 4 | `python server.py` | `project Model/capacity_model/` | 5002 |

---

## 📘 Usage Guide

### 1. Open the Application
Navigate to **http://localhost:3000** in your browser.

### 2. Landing Page
You'll see the **"Welcome to Aqua Forecast"** hero section with a rain animation and ocean-themed background. Click **"Explore Aqua Forecast"** to proceed.

### 3. Menu / Dashboard
The menu page presents three prediction cards:

| Card | Description | Requires |
|---|---|---|
| **Predict Capacity** | Predicts reservoir capacity percentage | Capacity model (port 5002) |
| **Predict Water Demand** | Forecasts water demand in units | Water demand model (port 5000) |
| **Predict Sector Wise Risk** | Assesses sector water risk level | Sector model (port 5001) |

### 4. Making Predictions
1. Click on any prediction card
2. Fill in the required input fields
3. Click the **Predict / Assess** button
4. View the results displayed on the same page

> ⚠️ If a Flask model server is not running, you'll see an error: **"Error connecting to prediction server."** — Make sure the corresponding Flask server is running.

---

## 🔗 API Endpoints

### Water Demand Prediction
```http
POST http://127.0.0.1:5000/predict
Content-Type: application/json

{
  "Temperature": 35,
  "Rainfall": 10,
  "Population": 2000000,
  "Reservoir_Level": 75,
  "Water_Tariff": 15,
  "Holiday": 0,
  "lag_1": 500,
  "lag_7": 480,
  "City": "Bhopal",
  "Season": "Summer"
}
```
**Response:**
```json
{ "prediction": 523 }
```

### Reservoir Capacity Prediction
```http
POST http://127.0.0.1:5002/predict_capacity
Content-Type: application/json

{
  "Rainfall_mm": 150,
  "Inflow_cumecs": 1200,
  "Outflow_cumecs": 800,
  "Runoff_Factor": 0.4
}
```
**Response:**
```json
{ "predicted_capacity_percentage": 72.35 }
```

### Sector Risk Assessment
```http
POST http://127.0.0.1:5001/predict_risk
Content-Type: application/json

{
  "population": 500000,
  "capacity": 1000,
  "inflow": 50,
  "outflow": 40,
  "reservoirlevel": 60
}
```
**Response:**
```json
{
  "predicted_demand": 1234.56,
  "risk_level": "Medium Risk",
  "risk_ratio": 0.65
}
```
---

## 🔧 Troubleshooting

| Issue | Solution |
|---|---|
| `npm error Missing script: "start"` | Run `npm run dev` instead, or ensure `package.json` has a `start` script |
| `ModuleNotFoundError: No module named 'flask'` | Run `pip install flask flask-cors` |
| `ModuleNotFoundError: No module named 'seaborn'` | Run `pip install seaborn` (only needed for `app.py` training script) |
| `Error connecting to prediction server` | Ensure the corresponding Flask server is running on the correct port |
| Port already in use | Kill the process using the port or change the port in the Flask server file |
| `node --watch` not working | Upgrade Node.js to v18+ (the `--watch` flag requires Node 18+) |

---

## 👥 Team
Prayagi sahajwani,Sanskrati Kachole Sheetal narwariya, Sejal Soni
**Minor Project — Aqua Forecast**
