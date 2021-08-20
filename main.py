from fastapi import FastAPI, Query
# from pydantic import BaseModel
import random
from typing import List, Optional

from tools import tools

tool = tools()
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
def get_random_choice(values: str, amount: Optional[int] = 1):
    values = tool.parse_string_list(values)
    if (amount > len(values)):
        return ["Error, amount greater than the length of the valuesList"]
    response = random.sample(values, amount)
    return get_response(response)


@app.get("/coinFlip")
def get_coin_flip():
    return get_response(random.choice(["Heads", "Tail"]))
