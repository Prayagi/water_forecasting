const express = require('express');
const app = express();
const path = require('path');
const axios = require('axios');

app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, 'public')));
app.set('view engine', 'ejs');

// Python Flask API URL
const PYTHON_API_URL = 'http://localhost:5000';

app.get('/', (req, res) => {
    res.render('in.ejs');
});

// Dashboard route (button ke baad ye open hoga)
app.get('/menu', (req, res) => {
    res.render('menu.ejs');
});

// Prediction form route
app.get('/predict', (req, res) => {
    res.render('predict.ejs');
});

// Risk assessment page route
app.get('/risk-assessment', (req, res) => {
    res.render('risk_assessment.ejs');
});

// Handle prediction request
app.post('/predict', async (req, res) => {
    try {
        const today = new Date();
        const weekdayIndex = (today.getDay() + 6) % 7; // Convert JS Sunday=0 to Monday=0

        const predictionData = {
            Temperature: parseFloat(req.body.temperature),
            Rainfall: parseFloat(req.body.rainfall),
            Population: parseInt(req.body.population),
            Reservoir_Level: parseFloat(req.body.reservoirLevel),
            Water_Tariff: parseFloat(req.body.waterTariff),
            Holiday: req.body.holiday === 'yes' ? 1 : 0,
            year: today.getFullYear(),
            month: today.getMonth() + 1,
            day: today.getDate(),
            weekday: weekdayIndex,
            lag_1: parseFloat(req.body.lag1),
            lag_7: parseFloat(req.body.lag7),
            [`City_${req.body.city}`]: 1,
            [`Area_Type_${req.body.areaType}`]: 1,
            [`Weather_${req.body.weather}`]: 1,
            [`Season_${req.body.season}`]: 1
        };

        // Fill missing city columns with 0
        const cities = ['Bhopal', 'Gwalior', 'Indore', 'Jabalpur', 'Ujjain'];
        cities.forEach(city => {
            if (city !== req.body.city) {
                predictionData[`City_${city}`] = 0;
            }
        });

        // Fill missing area type columns with 0
        const areaTypes = ['Rural', 'Urban'];
        areaTypes.forEach(type => {
            if (type !== req.body.areaType) {
                predictionData[`Area_Type_${type}`] = 0;
            }
        });

        // Fill missing weather columns with 0
        const weathers = ['Cloudy', 'Rainy', 'Sunny'];
        weathers.forEach(weather => {
            if (weather !== req.body.weather) {
                predictionData[`Weather_${weather}`] = 0;
            }
        });

        // Fill missing season columns with 0
        const seasons = ['Monsoon', 'Summer', 'Winter'];
        seasons.forEach(season => {
            if (season !== req.body.season) {
                predictionData[`Season_${season}`] = 0;
            }
        });

        // Call Python API
        const response = await axios.post(`${PYTHON_API_URL}/predict`, predictionData);
        const prediction = response.data.prediction;

        res.render('result.ejs', {
            prediction: prediction,
            inputData: req.body
        });

    } catch (error) {
        console.error('Prediction error:', error.message);
        res.render('error.ejs', {
            error: 'Failed to get prediction. Please make sure the Python server is running.'
        });
    }
});

app.listen(3000, () => {
    console.log('Node.js server is running on port 3000');
    console.log('Make sure Python Flask server is running on port 5000');
}); 

