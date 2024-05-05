import pytest
import requests

BASE_URL='http://127.0.0.1:5000'
tasks = []

def test_create_task():
  new_task_data ={
    "title": "Nova tarefa",
    "description": "Descrição nova da tarefa"
  }
  response = requests.post(f"{BASE_URL}/tasks", json=new_task_data)
  res_json = response.json()

  assert response.status_code == 200
  assert "message" in res_json 
  assert "id" in res_json 

  tasks.append(res_json['id'])

def test_get_tasks():
  response = requests.get(f"{BASE_URL}/tasks")
  res_json = response.json()

  assert response.status_code == 200
  assert "tasks" in res_json
  assert "total_tasks" in res_json

def test_get_task():
  if tasks:
    task_id = tasks[0]
    response = requests.get(f"{BASE_URL}/tasks/{task_id}")
    res_json = response.json()

    assert response.status_code == 200
    assert "completed" in res_json
    assert "title" in res_json
    assert "description" in res_json
    assert "id" in res_json
    assert res_json['id'] == task_id

def test_update_task():
  if tasks:
    task_id = tasks[0]
    updated_task={
      "title": "Nova tarefa",
      "description": "Descrição nova da tarefa atualizada",
      "completed": True
    }
    response = requests.put(f"{BASE_URL}/tasks/{task_id}", json=updated_task)
    res_json = response.json()

    assert response.status_code == 200
    assert "message" in res_json
    assert res_json['message'] == "Tarefa atualizada com sucesso."

    response = requests.get(f"{BASE_URL}/tasks/{task_id}")
    res_json = response.json()
    assert res_json['title'] == updated_task['title']
    assert res_json['description'] == updated_task['description']
    assert res_json['completed'] == updated_task['completed']



def test_delete_task():
  if tasks:
    task_id = tasks[0]
    response = requests.delete(f"{BASE_URL}/tasks/{task_id}")
    res_json = response.json()

    assert response.status_code == 200
    assert "message" in res_json
    assert res_json['message'] == "Tarefa deletada com sucesso."

    response = requests.get(f"{BASE_URL}/tasks/{task_id}")
    assert response.status_code == 404
