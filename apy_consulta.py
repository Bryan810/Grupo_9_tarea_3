from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd

app = Flask(__name__)
CORS(app)

modelo = joblib.load("modelo_ciberataques.pkl")
columnas = joblib.load("columnas.pkl")
le_attack = joblib.load("le_attack.pkl")
le_industry = joblib.load("le_industry.pkl")

@app.route("/")
def home():
    return {"status": "API de consulta de ciberataques activa"}

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    
    try:
        industry_num = le_industry.transform([data["Target Industry"]])[0]
        
        df = pd.DataFrame([{
            "Target Industry": industry_num,
            "Year": data["Year"],
            "Number of Affected Users": data["Number of Affected Users"]
        }], columns=columnas)
        
        pred_num = modelo.predict(df)[0]
        pred_label = le_attack.inverse_transform([pred_num])[0]
        
        return jsonify({"prediction": pred_label})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
