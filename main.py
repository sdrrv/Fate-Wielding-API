from fastapi import FastAPI, Query
#from pydantic import BaseModel
import random
from typing import List, Optional

app = FastAPI()


def get_response(response):
    return {
        "response": response,
        "type": str(type(response))
    }


@app.get("/")
def index():
    return {"NAME": "Fate Wielding API",
            "VERSION": "0.0.2"}


# ex /randomNumberBetween/0/10
@app.get("/randomNumberBetween")
def get_random_number_between_two_values(firstValue: int, secondValue: int):
    response = random.randint(firstValue, secondValue)
    return get_response(response)


@app.get("/randomChoice")
def get_random_choice(amount: Optional[int] = Query(None), value: List[str] = Query(None)):
    if not amount:
        amount = 1
    if (amount > len(value)):
        return ["Error, amount greater than the length of the valuesList"]
    response = random.sample(value, amount)
    return get_response(response)
