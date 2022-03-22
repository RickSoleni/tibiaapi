from pydantic import BaseModel


class Monster(BaseModel):
    name: str
    hp: int
    exp: int
    charms: int
    speed: int
    armor: int
    abilities: int


class MonsterModify(BaseModel):
    name: str
    hp: int
    exp: int
    charms: int
    speed: int
    armor: int
    abilities: int
