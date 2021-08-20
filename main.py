from fastapi import FastAPI, Query
#from pydantic import BaseModel
import random
from typing import List, Optional

app = FastAPI()


@app.get("/")
def index():
    return {"NAME": "Fate Wielding API",
            "VERSION": "0.0.2"}


# ex /randomNumberBetween/0/10
@app.get("/randomNumberBetween")
def get_random_number_between_two_values(firstValue: int, secondValue: int):
    return {"response": random.randint(firstValue, secondValue),
            "type": "List"}


@app.get("/randomChoice")
def get_random_choice(amount: Optional[int] = Query(None), value: List[str] = Query(None)):
    if not amount:
        amount = 1
    if (amount > len(value)):
        return ["Error, amount greater than the length of the valuesList"]
    return {"response": random.sample(value, amount),
            "type": "float"}
