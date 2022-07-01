from urllib import response
from fastapi.testclient import TestClient
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__),'../'))

from main import app

client = TestClient(app)

USER_LOGIN = {
    "username":"username",
    "password":"password"
}

USER_NO_LOGIN = {
    "username":"password",
    "password":"username"
}

# tests views 1
def test_get_patent_list():
    token = client.post('/login/',data=USER_LOGIN)
    assert token.status_code == 200
    assert token.json()["token_type"] == "bearer"

    headers = {
        "Authorization":f"Bearer {token.json()['access_token']}"
    }

    response = client.get('/patent/',headers=headers)
    assert response.status_code == 200


def test_get_patent_list_no_login():
    token = client.post('/login/',data=USER_NO_LOGIN)
    assert token.status_code == 404



# tests views 2
def test_get_patent_vehicle():
    token = client.post('/login/',data=USER_LOGIN)
    assert token.status_code == 200
    assert token.json()["token_type"] == "bearer"

    headers = {
        "Authorization":f"Bearer {token.json()['access_token']}"
    }
    id = 1
    response = client.get('/patent/{}'.format(id),headers=headers)
    assert response.status_code == 200

def test_get_no_patent_vehicle():
    token = client.post('/login/',data=USER_LOGIN)
    assert token.status_code == 200
    assert token.json()["token_type"] == "bearer"

    headers = {
        "Authorization":f"Bearer {token.json()['access_token']}"
    }
    id = 123456789
    response = client.get('/patent/{}'.format(id),headers=headers)
    assert response.status_code == 200


#test views 3 
def test_get_patent_id():
    token = client.post('/login/',data=USER_LOGIN)
    assert token.status_code == 200
    assert token.json()["token_type"] == "bearer"

    headers = {
        "Authorization":f"Bearer {token.json()['access_token']}"
    }
    placa = "MMM029"
    response = client.get('/patent/placa/{}'.format(placa),headers=headers)
    assert response.status_code == 200

def test_get_no_patent_id():
    token = client.post('/login/',data=USER_LOGIN)
    assert token.status_code == 200
    assert token.json()["token_type"] == "bearer"

    headers = {
        "Authorization":f"Bearer {token.json()['access_token']}"
    }
    placa = "MMA029"
    response = client.get('/patent/placa/{}'.format(placa),headers=headers)
    assert response.status_code == 200