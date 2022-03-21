from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import JSONResponse
from typing import Optional
from tibiadatabase import Monsters


app = FastAPI()


class Monster(BaseModel):
    name: str
    hp: int
    exp: int
    charms: int
    speed: int
    armor: int
    abilities: int


class MonsterModify(BaseModel):
    name: Optional[str]
    hp: Optional[int]
    exp: Optional[int]
    charms: Optional[int]
    speed: Optional[int]
    armor: Optional[int]
    abilities: Optional[int]


@app.post('/monster')
def create_monster(monster: Monster):
    query = Monsters.insert(
        {
            Monsters.name: monster.name,
            Monsters.hp: monster.hp,
            Monsters.exp: monster.exp,
            Monsters.charms: monster.charms,
            Monsters.speed: monster.speed,
            Monsters.armor: monster.armor,
            Monsters.abilities: monster.abilities,
        }
    )
    query.execute()

    return JSONResponse({'Message': 'Monster Created'}, 201)


@app.get('/monster/{name}')
def get_monster(name: str):
    monster = Monsters.get_as_dict(Monsters.name == name)

    if monster:

        return JSONResponse({'Monster': monster}, 200)

    return JSONResponse({'Message': 'Monster Not Found'}, 404)


@app.put('/monster/{name}')
def put_monster(name: str, modifymonster: MonsterModify):

    monster = Monsters.get_as_dict(Monsters.name == name)

    if not monster:
        return JSONResponse({'Message': 'Monster Not Found'}, 404)

    if modifymonster.name:
        query = Monsters.update({Monsters.name: modifymonster.name}).where(
            Monsters.name == name
        )
        query.execute()
        return JSONResponse({'Message': 'Name modified'})

    if modifymonster.hp:
        query = Monsters.update({Monsters.hp: modifymonster.hp}).where(
            Monsters.name == name
        )
        query.execute()
        return JSONResponse({'Message': 'HP modified'})

    if modifymonster.exp:
        query = Monsters.update({Monsters.exp: modifymonster.exp}).where(
            Monsters.name == name
        )
        query.execute()
        return JSONResponse({'Message': 'EXP modified'})

    if modifymonster.charms:
        query = Monsters.update({Monsters.charms: modifymonster.charms}).where(
            Monsters.name == name
        )
        query.execute()
        return JSONResponse({'Message': 'Charms modified'})

    if modifymonster.speed:
        query = Monsters.update({Monsters.speed: modifymonster.speed}).where(
            Monsters.name == name
        )
        query.execute()
        return JSONResponse({'Message': 'Speed modified'})

    if modifymonster.armor:
        query = Monsters.update({Monsters.armor: modifymonster.armor}).where(
            Monsters.name == name
        )
        query.execute()
        return JSONResponse({'Message': 'Armor modified'})

    if modifymonster.abilities:
        query = Monsters.update(
            {Monsters.abilities: modifymonster.abilities}
        ).where(Monsters.name == name)
        query.execute()
        return JSONResponse({'Message': 'Abilities modified'})


@app.delete('/monster/{name}')
def delete_monster(name: str):

    query = Monsters.delete().where(Monsters.name == name)

    if query.execute():
        return JSONResponse({'Message': 'Monster Deleted'}, 200)

    return JSONResponse({'Message': 'Monster Not found'}, 404)
