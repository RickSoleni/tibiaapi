from fastapi import FastAPI
from models import Monster, MonsterModify
from starlette.responses import JSONResponse
from services import create, read, update, delete


app = FastAPI()


@app.post('/monster')
def create_monster(monster: Monster):

    created = create(monster.dict())
    if not created:
        return JSONResponse({'Message': 'Invalid Input: you can\'t send a duplicated monster name'}, 400)

    return JSONResponse({'Message': 'Monster Created'}, 201)


@app.get('/monster/{name}')
def get_monster(name: str):

    monster = read(name)

    if not monster:
        return JSONResponse({'Message': 'Monster Not Found'}, 404)
    return JSONResponse({'Monster': monster}, 200)


@app.put('/monster/{name}')
def update_monster(name: str, modifymonster: MonsterModify):

    is_modified = bool(update(name, modifymonster.dict(exclude_unset=True)))

    if not is_modified:
        return JSONResponse({'Message': 'Monster Not Found'}, 404)
    return JSONResponse({'Message': 'Monster Modified'}, 200)


@app.delete('/monster/{name}')
def delete_monster(name: str):

    is_deleted = bool(delete(name))

    if not is_deleted:
        return JSONResponse({'Message': 'Monster Not Found'}, 404)
    return JSONResponse({'Message': 'Monster Deleted'}, 200)
