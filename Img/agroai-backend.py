import os
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
import joblib
import json

app = Flask(__name__)
CORS(app)

# Simulated Machine Learning Models and Data
class AgroAIBackend:
    def __init__(self):
        # Crop Recommendation Model (Simulated)
        self.crop_recommendation_model = self._train_crop_recommendation_model()
        
        # Weather Data (Simulated)
        self.weather_data = self._load_weather_data()
        
        # Pest Alert System (Simulated)
        self.pest_alerts = self._generate_pest_alerts()
        
        # Market Price Predictions (Simulated)
        self.market_prices = self._generate_market_prices()

    def _train_crop_recommendation_model(self):
        """
        Simulate a crop recommendation model training
        Uses RandomForestRegressor as a placeholder
        """
        # Simulated training data
        np.random.seed(42)
        X = np.random.rand(100, 5)  # 5 features: soil_type, moisture, temperature, rainfall, nutrients
        y = np.random.choice(['Wheat', 'Rice', 'Corn', 'Soybean', 'Potato'], size=100)
        
        model = RandomForestRegressor()
        model.fit(X, y)
        return model

    def _load_weather_data(self):
        """
        Generate simulated weather data for different regions
        """
        regions = ['North', 'South', 'East', 'West', 'Central']
        weather_data = {
            region: {
                'temperature': np.random.uniform(15, 35),
                'humidity': np.random.uniform(50, 90),
                'rainfall_probability': np.random.uniform(0, 100)
            } for region in regions
        }
        return weather_data

    def _generate_pest_alerts(self):
        """
        Generate simulated pest alerts
        """
        crops = ['Wheat', 'Rice', 'Corn', 'Soybean', 'Potato']
        pest_alerts = {
            crop: {
                'risk_level': np.random.choice(['Low', 'Medium', 'High']),
                'recommended_action': np.random.choice(['Monitor', 'Spray', 'Isolate'])
            } for crop in crops
        }
        return pest_alerts

    def _generate_market_prices(self):
        """
        Generate simulated market prices for different crops
        """
        crops = ['Wheat', 'Rice', 'Corn', 'Soybean', 'Potato']
        market_prices = {
            crop: {
                'current_price': np.random.uniform(10, 100),
                'price_trend': np.random.choice(['Rising', 'Stable', 'Falling'])
            } for crop in crops
        }
        return market_prices

# Initialize Backend
backend = AgroAIBackend()

@app.route('/crop-recommendation', methods=['POST'])
def crop_recommendation():
    """
    AI-powered crop recommendation endpoint
    """
    try:
        data = request.json
        # Extract features: soil_type, moisture, temperature, rainfall, nutrients
        features = [
            data.get('soil_type', 0.5),
            data.get('moisture', 0.5),
            data.get('temperature', 25),
            data.get('rainfall', 50),
            data.get('nutrients', 0.5)
        ]
        
        # Predict recommended crop
        recommended_crop = backend.crop_recommendation_model.predict([features])[0]
        
        return jsonify({
            'recommended_crop': recommended_crop,
            'confidence': np.random.uniform(0.7, 0.95)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/weather-alerts', methods=['GET'])
def weather_alerts():
    """
    Provide weather alerts for different regions
    """
    region = request.args.get('region', 'North')
    weather_info = backend.weather_data.get(region, {})
    
    return jsonify({
        'region': region,
        'temperature': weather_info.get('temperature'),
        'humidity': weather_info.get('humidity'),
        'rainfall_probability': weather_info.get('rainfall_probability'),
        'alert_level': 'Moderate' if weather_info.get('rainfall_probability', 0) > 70 else 'Low'
    })

@app.route('/pest-alerts', methods=['GET'])
def pest_alerts():
    """
    Provide pest alerts for different crops
    """
    crop = request.args.get('crop', 'Wheat')
    pest_alert = backend.pest_alerts.get(crop, {})
    
    return jsonify({
        'crop': crop,
        'risk_level': pest_alert.get('risk_level', 'Low'),
        'recommended_action': pest_alert.get('recommended_action', 'Monitor')
    })

@app.route('/market-prices', methods=['GET'])
def market_prices():
    """
    Retrieve market prices for crops
    """
    crop = request.args.get('crop', 'Wheat')
    market_price = backend.market_prices.get(crop, {})
    
    return jsonify({
        'crop': crop,
        'current_price': market_price.get('current_price'),
        'price_trend': market_price.get('price_trend')
    })

@app.route('/health', methods=['GET'])
def health_check():
    """
    Simple health check endpoint
    """
    return jsonify({
        'status': 'healthy',
        'version': '1.0.0',
        'services': ['crop_recommendation', 'weather_alerts', 'pest_alerts', 'market_prices']
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)

# Requirements File (requirements.txt)
"""
flask==2.1.0
flask-cors==3.0.10
numpy==1.22.3
pandas==1.4.2
scikit-learn==1.0.2
joblib==1.1.0
"""

# README.md for Setup
"""
# AgroAI Backend

## Setup Instructions

1. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Run the application
```bash
python app.py
```

## API Endpoints

- `/crop-recommendation` (POST): AI-powered crop recommendations
- `/weather-alerts` (GET): Regional weather information
- `/pest-alerts` (GET): Crop-specific pest alerts
- `/market-prices` (GET): Current market prices
- `/health` (GET): System health check

## Example Curl Requests

1. Crop Recommendation:
```bash
curl -X POST http://localhost:5000/crop-recommendation \
     -H "Content-Type: application/json" \
     -d '{"soil_type": 0.7, "moisture": 0.6, "temperature": 25, "rainfall": 60, "nutrients": 0.5}'
```
"""
