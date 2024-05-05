from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)

tasks = []
task_id_control = 1

@app.route('/tasks', methods=['POST'])
def create_task():
  global task_id_control
  data = request.get_json()
  new_task = Task(task_id_control, data['title'], data['description'])
  task_id_control += 1
  tasks.append(new_task)
  print(tasks)
  return jsonify({ "message": "Nova tarefa criada com sucesso!" })

@app.route('/tasks', methods=['GET'])
def get_tasks():
  task_list = [task.to_dict() for task in tasks]

  return jsonify({
    "tasks": task_list,
    "total_tasks": len(task_list)
  })

@app.route('/tasks/<int:id>', methods=['GET'])
def get_task_by_id(id):
  task = None
  for t in tasks:
    if t.id == id:
      return jsonify(t.to_dict())

  return jsonify({ "message": f"Atividade com id {id} não existe." }), 404


if __name__ == "__main__":
  app.run(debug=True)