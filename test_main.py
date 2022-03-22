import pytest
from starlette.testclient import TestClient
from main import app

teste = TestClient(app)



@pytest.fixture()
def payload():
    return  {
        'name': 'Dragon',
        'hp': 1200,
        'exp': 720,
        'charms': 25,
        'speed': 103,
        'armor': 36,
        'abilities': 1,
    }

def test_post_with_a_valid_payload(payload):

    response = teste.post('/monster', json=payload)
    assert response.json() == {'Message': 'Monster Created'}
    assert response.status_code == 201
    response = teste.get('/monster/Dragon')
    res_json = response.json()
    assert res_json['Monster'] == payload


def test_post_with_a_invalid_payload():

    invalid_payload = {'lambe_minhas_bola': 'hahaha'}

    response = teste.post('/monster', json=invalid_payload)

    assert response.status_code == 422


def test_get_name_with_a_valid_name(payload):

    response = teste.post('/monster', json=payload)

    response = teste.get('/monster/Dragon')

    assert response.status_code == 200
    assert 'Monster' in response.json()


def test_get_name_with_a_invalid_name():

    response = teste.get('/monster/Dragooooon')
    assert response.status_code == 404
    assert response.json() == {'Message': 'Monster Not Found'}


def test_put_with_a_valid_name():

    name = 'Dragon'
    previous_monster = teste.get(f'/monster/{name}')

    assert previous_monster.status_code == 200

    response = teste.put(f'/monster/{name}', json={'name': 'Dragon Lord'})
    new_monster = teste.get('/monster/Dragon Lord')

    assert previous_monster.json() != new_monster.json()
    assert response.json() == {'Message': 'Monster Modified'}
    assert response.status_code == 200


def test_put_with_a_invalid_name():

    name = 'Abluble'
    response = teste.get(f'/monster/{name}')

    assert response.status_code == 404
    response = teste.put(f'/monster/{name}', json={'name': 'ablubleeee'})

    assert response.json() == {'Message': 'Monster Not Found'}
    assert response.status_code == 404


def test_delete_with_a_valid_name():

    name = 'Dragon Lord'
    response = teste.get(f'/monster/{name}')
    assert response.status_code == 200

    response = teste.delete(f'/monster/{name}')
    assert response.status_code == 200
    assert response.json() == {'Message': 'Monster Deleted'}
    
    deleted = teste.get(f'/monster/Dragon Lord')    
    assert deleted.status_code == 404



def test_delete_with_a_invalid_name():

    name = 'Abluble'
    response = teste.get(f'/monster/{name}')

    assert response.status_code == 404
    response = teste.delete(f'/monster/{name}')

    assert response.json() == {'Message': 'Monster Not Found'}
    assert response.status_code == 404
