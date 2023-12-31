from unittest.mock import patch
from flask import Flask, jsonify
from src.blueprints.blacklist_blueprint import blacklist_blueprint
from src.errors.errors import ApiError

app = Flask(__name__)
app.register_blueprint(blacklist_blueprint)
@app.errorhandler(ApiError)
def handle_exception(err):
    response = {
        "msg": err.description
    }
    return jsonify(response), err.code

client = app.test_client()

BEARER_TOKEN = "123"


@patch('src.blueprints.blacklist_blueprint.AddToBlacklistCommand')
def test_add_to_blacklist_success(mock_add_to_blacklist_command):
    mock_instance = mock_add_to_blacklist_command.return_value
    mock_instance.execute.return_value = {'message': 'Email added to the blacklist'}

    response = client.post('/blacklists', json={
        "email": "test@example.com",
        "app_uuid": "123",
        "blocked_reason": "fraudulent activity"
    }, headers={"Authorization": f"Bearer {BEARER_TOKEN}"})

    assert response.status_code == 201
    assert response.json == {'message': 'Email added to the blacklist'}

def test_add_to_blacklist_invalid_token():
    response = client.post('/blacklists', json={
        "email": "test@example.com",
        "app_uuid": "123",
        "blocked_reason": "fraudulent activity"
    }, headers={"Authorization": f"Bearer wrongtoken"})

    assert response.status_code == 401

def test_add_to_blacklist_invalid_data():
    response = client.post('/blacklists', json={
        "blocked_reason": "fraudulent activity"
    }, headers={"Authorization": f"Bearer {BEARER_TOKEN}"})

    assert response.status_code == 400

@patch('src.blueprints.blacklist_blueprint.CheckBlacklistCommand')
def test_check_blacklist_success(mock_check_blacklist_command):
    mock_instance = mock_check_blacklist_command.return_value
    mock_instance.execute.return_value = (True, "fraudulent activity")

    response = client.get('/blacklists/test@example.com', headers={"Authorization": f"Bearer {BEARER_TOKEN}"})

    assert response.status_code == 200
    assert response.json == {
        "email": "test@example.com",
        "blocked": True,
        "blocked_reason": "fraudulent activity"
    }


def test_health_check():
    response = client.get('/ping')

    assert response.status_code == 200
    assert response.json == {'message': 'pong'}
