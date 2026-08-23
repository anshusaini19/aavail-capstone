from flask import Flask, jsonify, request
import pandas as pd
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "AAVAIL Revenue Forecasting API is running successfully."})

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        country = data.get("country", "all")
        target_date = data.get("target_date")
        
        # Simulated prediction logic based on inputs
        if country.lower() == "all":
            prediction = 15000.00  # Combined prediction placeholder
        else:
            prediction = 4500.00   # Single country prediction placeholder
            
        response = {
            "country": country,
            "target_date": target_date,
            "predicted_revenue": prediction,
            "status": "success"
        }
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
