import pandas as pd
import os

def load_dataset():
    file_path = "uploads/creditcard.csv"

    if not os.path.exists(file_path):
        return None

    df = pd.read_csv(file_path)
    return df


def get_baseline_metrics():
    df = load_dataset()

    if df is None:
        return {"error": "Dataset not found"}

    total_transactions = len(df)
    fraud_cases = len(df[df["Class"] == 1])
    normal_cases = len(df[df["Class"] == 0])

    fraud_percentage = round((fraud_cases / total_transactions) * 100, 2)

    return {
        "total_transactions": total_transactions,
        "fraud_cases": fraud_cases,
        "normal_cases": normal_cases,
        "fraud_percentage": fraud_percentage
    }