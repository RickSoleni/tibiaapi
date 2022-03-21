from starlette.testclient import TestClient
from tibiadatabase import Monsters
from main import app

teste = TestClient(app)


def test_post_with_a_valid_payload():

    payload = {
        'name': 'Dragon',
        'hp': 1200,
        'exp': 720,
        'charms': 25,
        'speed': 103,
        'armor': 36,
        'abilities': 1,
    }

    response = teste.post('/monster', json=payload)
    assert response.json() == {'Message': 'Monster Created'}
    assert response.status_code == 201
    assert Monsters.get_as_dict(Monsters.name == 'Dragon')


def test_post_with_a_invalid_payload():

    invalid_payload = {'lambe_minhas_bola': 'hahaha'}

    response = teste.post('/monster', json=invalid_payload)

    assert response.status_code == 422


def test_get_name_with_a_valid_name():

    response = teste.get('/monster/Dragon')

    assert response.status_code == 200
    assert 'Monster' in response.json()


def test_get_name_with_a_invalid_name():

    response = teste.get('/monster/Dragooooon')
    assert response.status_code == 404
    assert response.json() == {'Message': 'Monster Not Found'}


def test_put_with_a_valid_name():

    name = 'Dragon'
    monster = Monsters.get_as_dict(Monsters.name == name)

    assert monster

    response = teste.put(f'/monster/{name}', json={'name': 'Dragon Lord'})

    assert monster != Monsters.get_as_dict(Monsters.name == name)

    assert response.json() == {'Message': 'Name modified'}

    assert response.status_code == 200


def test_put_with_a_invalid_id():

    name = 'Abluble'

    assert not Monsters.get_as_dict(Monsters.name == name)

    response = teste.put(f'/monster/{name}', json={'name': 'ablubleeee'})

    assert response.json() == {'Message': 'Monster Not Found'}

    assert response.status_code == 404


def test_delete_with_a_valid_name():

    name = 'Dragon Lord'

    assert Monsters.get_as_dict(Monsters.name == name)

    response = teste.delete(f'/monster/{name}')

    assert not Monsters.get_as_dict(Monsters.name == name)

    assert response.status_code == 200

    assert response.json() == {'Message': 'Monster Deleted'}


def test_delete_with_a_invalid_name():

    name = 'Abluble'

    assert not Monsters.get_as_dict(Monsters.name == name)

    response = teste.delete(f'/monster/{name}')

    assert response.status_code == 404

    assert response.json() == {'Message': 'Monster Not found'}
