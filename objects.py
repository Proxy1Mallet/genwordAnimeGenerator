from typing import List
from pydantic import BaseModel, Field

class Anime(BaseModel):
    nameRu: str
    nameEn: str

class Words(BaseModel):
    word: str
    wData: str

class Winged(BaseModel):
    phrase: str
    source: str

class Ingridients(BaseModel):
    ingridients: str

class AlcoholDrinking(BaseModel):
    nameRu: str
    nameEn: str
    typeAlcohol: str

class Alias(BaseModel):
    alias: str

class Slogan:
    slogan: str

class Login:
    result: dict[str]