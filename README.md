# Aqua Forecast - Water Demand Prediction System

A complete web application that integrates a Node.js frontend with a Python machine learning backend for predicting water demand using AI.

## Features

- **Modern Web Interface**: Beautiful, responsive UI built with Express.js and EJS
- **AI-Powered Predictions**: Machine learning model trained on water demand data
- **Real-time Integration**: Seamless communication between Node.js and Python Flask API
- **Comprehensive Input Form**: All necessary parameters for accurate predictions
- **Detailed Results**: Prediction results with input summary and AI insights

## Project Structure

```
Minor-project/                    # Node.js Web Application
├── index.js                      # Main Express server
├── package.json                  # Node.js dependencies
├── views/                        # EJS templates
│   ├── in.ejs                    # Landing page
│   ├── menu.ejs                  # Dashboard
│   ├── predict.ejs               # Prediction form
│   ├── result.ejs                # Results page
│   └── error.ejs                 # Error page
└── public/                       # Static assets
    ├── CSS_File/                 # Stylesheets
    └── JavaScript_File/          # Client-side scripts

project Model/WaterDemandPrediction_Model/  # Python ML Model
├── app.py                        # Flask API server
├── water_model.pkl              # Trained ML model
├── columns.pkl                  # Model feature columns
├── requirements.txt             # Python dependencies
└── model.ipynb                  # Jupyter notebook with model training
```

## Installation & Setup

### Prerequisites

- Node.js (v14 or higher) - Download from https://nodejs.org/
- Python (v3.8 or higher) with packages: flask, flask-cors, joblib, pandas, scikit-learn

### Quick Start

1. **Download/Unzip the project**

2. **Install Python dependencies** (if not already installed):
   ```bash
   pip install flask flask-cors joblib pandas scikit-learn
   ```

3. **Install Node.js dependencies**:
   ```bash
   cd Minor-project
   npm install
   ```

4. **Run the integrated setup script**:
   ```bash
   # Windows
   start_servers.bat

   # Or manually:
   # Terminal 1 - Python API
   cd "project Model/WaterDemandPrediction_Model"
   python app.py

   # Terminal 2 - Node.js Web App
   cd "Minor-project"
   npm start
   ```

5. **Access the application**:
   - Web App: http://localhost:3000
   - API: http://localhost:5000

## Usage

1. **Landing Page**: Visit http://localhost:3000
2. **Dashboard**: Click the main button to access features
3. **Water Demand Prediction**: Click "Predict Water Demand" card
4. **Fill Form**: Enter all required parameters
5. **Get Results**: View AI-powered prediction with insights

## API Endpoints

### Python Flask API (Port 5000)

- `POST /predict`: Get water demand prediction
  - Body: JSON with all model features
  - Response: `{"prediction": number}`

### Node.js Web App (Port 3000)

- `GET /`: Landing page
- `GET /menu`: Dashboard
- `GET /predict`: Prediction form
- `POST /predict`: Process prediction and show results

## Model Features

The AI model considers the following factors:

- **Weather**: Temperature, Rainfall, Weather condition, Season
- **Location**: City, Area Type (Urban/Rural)
- **Demographics**: Population
- **Infrastructure**: Reservoir Level, Water Tariff
- **Temporal**: Date features, Holiday status, Lag features
- **Historical**: Previous day and 7-day ago demand

## Technologies Used

### Frontend
- **Node.js** with **Express.js**
- **EJS** templating
- **CSS3** with modern gradients and animations
- **Responsive Design**

### Backend
- **Python Flask** API
- **Scikit-learn** Random Forest model
- **Pandas** for data processing
- **Joblib** for model serialization

### Machine Learning
- **Random Forest Regressor**
- **Feature Engineering** (lag features, one-hot encoding)
- **Time Series Analysis**

## Development

### Adding New Features

1. Update the Python model if needed
2. Modify the Node.js routes in `index.js`
3. Create/update EJS templates in `views/`
4. Update CSS in `public/CSS_File/`

### Model Retraining

1. Update data in `mp_water_demand_4000_rows.csv`
2. Modify and run `model.ipynb`
3. Save new `water_model.pkl` and `columns.pkl`
4. Update `requirements.txt` if needed

## Troubleshooting

### Common Issues

1. **"Failed to get prediction"**
   - Ensure Python Flask server is running on port 5000
   - Check console for Python errors

2. **"Cannot find module"**
   - Run `npm install` in Minor-project directory

3. **"Python module not found"**
   - Run `pip install -r requirements.txt` in the Python directory

4. **Port conflicts**
   - Change ports in `index.js` (Node.js) or `app.py` (Python)

### Logs

- Node.js logs: Terminal running `npm start`
- Python logs: Terminal running `python app.py`

## Future Enhancements

- [ ] Additional prediction models (capacity, risk assessment)
- [ ] User authentication and data persistence
- [ ] Real-time data integration
- [ ] Advanced visualizations and charts
- [ ] Mobile app development
- [ ] API documentation with Swagger

## License

This project is developed as part of a minor project for educational purposes.

## Contact

For questions or support, please check the project documentation or create an issue.