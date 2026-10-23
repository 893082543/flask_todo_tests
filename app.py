from flask import Flask, jsonify, request

app = Flask(__name__)

todos = []
next_id = 1

@app.route('/todos', methods=['GET'])
def list_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def create_todo():
    global next_id
    data = request.get_json()
    todo = {
        'id': next_id,
        'title': data['title'],
        'completed': data.get('completed', False)
    }
    todos.append(todo)
    next_id += 1
    return jsonify(todo), 201

if __name__ == '__main__':
    app.run(debug=True, port=5000)