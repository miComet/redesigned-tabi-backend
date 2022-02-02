from typing import Optional
from pydantic import BaseModel


class Image(BaseModel):
    id: Optional[int] = -1
    image_url: str
    title: str
    location: str
    season: str


class Spot(BaseModel):
    id: Optional[int] = -1
    image_url: str
    title: str
    location: str
    destination_url: str


class User(BaseModel):
    id: Optional[int] = -1
    external_id: str
    vender: str
    gender: str
    email: str


class Record(BaseModel):
    id: Optional[int] = -1
    user: User
    ip: str
    likes: list[int]
    recommendations: list[int]
