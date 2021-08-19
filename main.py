from fastapi import FastAPI, Query
#from pydantic import BaseModel
import random
from typing import List, Optional
import uvicorn


# ------------------------------------------------------------------------------


def run():
    uvicorn.run(app, host='0.0.0.0')
# -------------------------------------------------------------------------------


app = FastAPI(docs_url=None, redoc_url=None)


@app.get("/")
def index():
    return {"key": "value"}


# ex /randomNumberBetween/0/10
@app.get("/randomNumberBetween/{firstValue}-{secondValue}")
def get_random_number_between_two_values(firstValue: int, secondValue: int):
    return random.randint(firstValue, secondValue)


@app.get("/randomChoice/")
def get_random_choice(amount: Optional[int] = Query(None), value: List[str] = Query(None)):
    if not amount:
        amount = 1
    if (amount > len(value)):
        return ["Error, amount greater than the length of the valuesList"]
    return random.sample(value, amount)


#print("Hello World")
# run()
# @app.get("/reOrderList")
