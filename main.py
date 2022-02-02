from typing import Optional
from fastapi import FastAPI
from lib.dataclasses import Image, Spot, Record

import json
import random

app = FastAPI()


@app.get("/pic", response_model=list[Image])
def getPic(pic_num: int):
    with open('example_data/images.json') as src:
        images = json.load(src)

    res = []
    for i in range(pic_num):
        res.append(Image(**random.choice(images)))

    return res


@app.get("/spot_recommendation", response_model=list[Spot])
def getSpotRecommendation(spot_num: Optional[int] = 1):
    with open('example_data/spots.json') as src:
        spots = json.load(src)

    res = []
    for i in range(spot_num):
        res.append(Spot(**random.choice(spots)))

    return res


@app.post("/record")
def createRecord(record: Record):
    print("Save record: " + str(record))
