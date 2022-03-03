from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()  # uvicorn rest_api:app --reload


class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


@app.get("/")
def read_root():
    return {"Welcome to the Tenma supply rest api": "72-2540"}


@app.get("/tenma/identification")
def read_item(item_id: int, voltage: Optional[int] = 0):
    return {"item_id": item_id, "voltage": voltage}


@app.get("/tenma/current")
def read_item(measurement_id: str, value: Optional[int] = 0):
    return {"measurement_id": measurement_id, "value": value}

@app.get("/tenma/voltage")
def read_item(measurement_id: str, value: Optional[int] = 0):
    return {"measurement_id": measurement_id, "value": value}

