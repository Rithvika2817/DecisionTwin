import pandas as pd
import os
import joblib

# Load trained model
model = joblib.load("fraud_model.pkl")


from app.routers.datasets import dataset_store

def load_dataset(dataset_id):

    if dataset_id not in dataset_store:
        return None

    file_path = dataset_store[dataset_id]

    if not os.path.exists(file_path):
        return None

    return pd.read_csv(file_path)


# Week 3 Analytics Function
def get_baseline_metrics(dataset_id):
    df = load_dataset(dataset_id)

    if df is None:
        return {"error": "Dataset not found"}

    total_rows = len(df)

    total_revenue = 0

    if "revenue" in df.columns:
        total_revenue = float(df["revenue"].sum())

    return {
        "total_rows": total_rows,
        "total_revenue": total_revenue
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
