import json

import requests
import jsonschema

from json_schemas.utils import load_schema


def test_get_status_code_ok():
    response = requests.get(url="https://reqres.in/api/users")

    assert response.status_code == 200


def test_get_status_per_page():
    response = requests.get(url="https://reqres.in/api/users", params={'per_page': 1})

    assert response.status_code == 200
    assert len(response.json()['data']) == 1
    assert response.json()['per_page'] == 1


def test_headers():
    response = requests.get(url="https://reqres.in/api/users", headers={'Accept': '*/*'})

    assert response.status_code == 200


def test_post_users():
    response = requests.post(
        url="https://reqres.in/api/users",
        json={
            "name": "morpheus",
            "job": "leader"
        }
    )

    schema = load_schema('post_users.json')
    assert response.status_code == 201
    # assert response.json()['name'] == 'morpheus'
