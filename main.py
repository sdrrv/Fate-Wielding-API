from fastapi import FastAPI
from pydantic import BaseModel
import random


app = FastAPI()


@app.get("/")
def index():
    return {"key": "value"}


# ex /randomNumberBetween/0/10
@app.get("/randomNumberBetween/{firstValue}-{secondValue}")
def get_random_number_between_two_values(firstValue: int, secondValue: int):
    return random.randint(firstValue, secondValue)


# @app.get("/randomChoice/{listOfValues}")
# def get_random_choice(listOfValues: list):
#    return random.choice(listOfValues)
