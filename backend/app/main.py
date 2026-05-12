from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "DecisionTwin Backend Running"}

@app.get("/healthz")
def health():
    return {"status": "ok"}