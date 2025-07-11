from flask import Flask, request, jsonify
import joblib
import numpy as np
from utils.preprocessing import preprocess_input

app = Flask(__name__)

# Load model and preprocessing objects
package = joblib.load("model/diabetes_model_gb.pkl")
model = package["model"]
scaler = package["scaler"]
gender_map = package["gender_map"]
smoke_map = package["smoke_map"]
feature_order = package["feature_order"]

@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Diabetes Prediction API is running"}), 200

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    try:
        input_array = preprocess_input(data, feature_order, scaler, gender_map, smoke_map)
        proba = model.predict_proba(input_array)[0, 1]
        pred = int(proba >= 0.5)
        return jsonify({
            "prediction": "Diabetes" if pred else "No Diabetes",
            "confidence": round(proba * 100, 2)
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)
