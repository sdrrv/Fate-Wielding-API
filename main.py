from fastapi import FastAPI
from pydantic import BaseModel
import random


app = FastAPI()


@app.get("/")
def index():
    return {"key": "value"}


@app.get("/randomNumberBetween")
def get_random_number_between_two_values(firstValue: int, secondValue: int):
    return random.randint(firstValue, secondValue)
