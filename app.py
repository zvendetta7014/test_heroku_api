#!./venv/bin/python
from flask import abort

from flask import Flask, jsonify
app = Flask(__name__)


tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

@app.route('/')
def index():
    return "landing page. HW"

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})




@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

@app.route('/api/v1.0/<float:lat>@<float:longt>', methods=['GET'])
def get_coordinate(lat, longt):
    return jsonify({'speed': 45.0})

if __name__ == '__main__':
    app.run(debug=True)
    app.run(host=0.0.0.0, port=8090)

