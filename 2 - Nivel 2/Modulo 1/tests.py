import pytest
import requests


tasks = []
baseURL = "http://127.0.0.1:5000"
def test_create_task():

    new_task_data = {
        "title": "Criar uma tarefa",
        "description":"Criando uma tarefa"   
    }

    response = requests.post(f"{baseURL}/tasks", json=new_task_data)

    assert response.status_code == 200

    response_json = response.json()

    assert "Message" in response_json    
    assert "Id" in response_json

    tasks.append(response_json['Id'])

def test_get_tasks():

    response = requests.get(f"{baseURL}/tasks")
    assert response.status_code == 200

    response_json = response.json()

    assert 'tasks' in response_json
    assert 'total_tasks' in response_json

def test_get_task():

    if tasks:
        task_id = tasks[0]
        response = requests.get(f"{baseURL}/tasks/{task_id}")
        response_json = response.json()
        assert response.status_code == 200
        assert task_id == response_json["id"]

def test_update_task():
    if tasks:
        task_id = tasks[0]

        payload = {
            'title' : 'Título Atulizado',
            'description' : 'Descrição atualizado',
            'completed' : True
        }

        response = requests.put(f"{baseURL}/tasks/{task_id}", json=payload)

        assert response.status_code == 200
   
        response_json = response.json()

        assert 'Message' in response_json

        response = requests.get(f"{baseURL}/tasks/{task_id}")
        assert response.status_code == 200
        response_json = response.json()
        assert response_json["title"] == payload["title"]
        assert response_json['description'] == payload['description']
        assert response_json['completed'] == payload['completed']

def test_delete_task():
    if tasks:
        task_id = tasks[0]
        response = requests.delete(f"{baseURL}/tasks/{task_id}")

        assert response.status_code == 200

        response_json = response.json()

        assert "Message" in response_json

        response = requests.get(f"{baseURL}/tasks/{task_id}")

        assert response.status_code == 404