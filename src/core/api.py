from fastapi import FastAPI
from core.twitter import trends

app = FastAPI()

@app.get("/trends/{woe_id}")
def get_trends(woe_id):
    return trends(woe_id)
