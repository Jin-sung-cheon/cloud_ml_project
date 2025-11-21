from fastapi import FastAPI
from app.utils import optimize_tokens
from app.model import predict

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Edge-Optimized ML Transformer API"}

@app.post("/predict")
def inference(input_text: str):
    cleaned = optimize_tokens(input_text)
    result = predict(cleaned)
    return {
        "input": input_text,
        "optimized_input": cleaned,
        "prediction": result
    }
