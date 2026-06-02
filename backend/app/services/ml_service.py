import pandas as pd
import os
import joblib

# Load trained model
model = joblib.load("fraud_model.pkl")


def load_dataset():
    file_path = "uploads/creditcard.csv"

    if not os.path.exists(file_path):
        return None

    df = pd.read_csv(file_path)
    return df


# Week 3 Analytics Function
def get_baseline_metrics():
    df = load_dataset()

    if df is None:
        return {"error": "Dataset not found"}

    total_transactions = len(df)
    fraud_cases = len(df[df["Class"] == 1])
    normal_cases = len(df[df["Class"] == 0])

    fraud_percentage = round(
        (fraud_cases / total_transactions) * 100,
        2
    )

    return {
        "total_transactions": total_transactions,
        "fraud_cases": fraud_cases,
        "normal_cases": normal_cases,
        "fraud_percentage": fraud_percentage
    }


# Week 4 Prediction Function
def predict_fraud(data: dict):
    df = pd.DataFrame([data])

    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0].max()

    return {
        "prediction": int(prediction),
        "confidence": round(float(probability) * 100, 2)
    }