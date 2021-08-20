from fastapi import FastAPI, Query
# from pydantic import BaseModel
import random
from typing import List, Optional

from controllers.tools import tools


tool = tools()
app = FastAPI()


@app.get("/")
def index():
    return {"NAME": "Fate Wielding API",
            "VERSION": "0.0.2"}


# ex /randomNumberBetween/0/10
@app.get("/randomNumberBetween")
def random_number_between_two_values(firstValue: int, secondValue: int):
    response = random.randint(firstValue, secondValue)
    return tool.get_response(response)


@app.get("/randomChoice")
def random_choice(values: str, amount: Optional[int] = 1):
    values = tool.parse_string_list(values)
    if (amount > len(values)):
        return ["Error, amount greater than the length of the valuesList"]
    response = random.sample(values, amount)
    return tool.get_response(response)


@app.get("/coinFlip")
def coin_flip():
    coinFace = random.choice(["Head", "Tail"])
    coinImage = tool.get_coin_image(coinFace)
    return tool.get_response_image(coinFace,coinImage)


@app.get("/diceRoll")
def dice_roll():
    diceRoll = random.randint(1,6)
    diceImage = tool.get_dice_image(diceRoll)
    return tool.get_response_image(diceRoll, diceImage)