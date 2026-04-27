@echo off
echo Starting Aqua Forecast Servers...
echo.

echo Note: Python dependencies should already be installed.
echo If not, run: pip install flask flask-cors joblib pandas scikit-learn
echo.

echo Starting Python Flask API server...
start cmd /k "cd /d project Model\WaterDemandPrediction_Model && python app.py"

timeout /t 3 /nobreak > nul

echo Starting Node.js web server...
cd "Minor-project"
start cmd /k "cd /d Minor-project && npm start"

echo.
echo Servers are starting up...
echo - Python API: http://localhost:5000
echo - Web App: http://localhost:3000
echo.
echo Press any key to exit...
pause > nul