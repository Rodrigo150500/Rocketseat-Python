from flask import Flask, request, jsonify
from Models.task import Task


app = Flask(__name__)

#CRUD
#CREATE, READ, UPDATE, DELETE

tasks = []

task_id_count = 1

@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_count
    data = request.get_json()
    new_task = Task(id = task_id_count, title = data.get('title'), description= data.get('description', ''))
    tasks.append(new_task)
    task_id_count += 1
    print(tasks)
    return jsonify({
        "Message":"Nova tarefa criada com sucesso",
        "Id": new_task.id
        })

@app.route('/tasks', methods = ['GET'])
def get_tasks():
    list_task = [task.to_dict() for task in tasks]

    output = {
        "tasks" : list_task,
        "total_tasks" : len(list_task)
    }
    
    return output

@app.route('/tasks/<int:id>', methods = ["GET"])
def get_task_by_id(id):
    for task in tasks:
        if task.id == id:
            return jsonify(task.to_dict())
    return jsonify({"Message":"Arquivo não encontrado"}), 404


@app.route('/tasks/<int:id>', methods = ["PUT"])
def update_task(id):
    for task in tasks:
        if task.id == id:
            data = request.get_json()

            task.title = data.get('title')
            task.description = data.get('description')
            task.completed = data.get('completed')

            return jsonify({"Message": "Tarefa atualizada com sucesso!"})

    return jsonify({"Message": "Arquivo não encontrado"}), 404

@app.route('/tasks/<int:id>', methods = ["DELETE"])
def delete_task(id):
    encontrado = False
    for task in tasks:
        if task.id == id:
            encontrado = True
            break
    if encontrado == False:
        return jsonify({"Message":"Tarefa não encontrada"}), 404
    
    tasks.remove(task)
    return jsonify({"Message": "Tarefa Deletada"}), 200

if __name__ == '__main__':
    app.run(debug=True)