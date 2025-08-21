from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage (for demonstration)
todos = []
next_id = 1

# Create a todo
@app.route('/todos', methods=['POST'])
def create_todo():
    global next_id
    data = request.json
    todo = {
        "id": next_id,
        "title": data.get("title", "Untitled"),
        "description": data.get("description", ""),
        "read": False
    }
    todos.append(todo)
    next_id += 1
    return jsonify(todo), 201

# Get all todos
@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

# Update a todo
@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    data = request.json
    for todo in todos:
        if todo['id'] == todo_id:
            todo['title'] = data.get('title', todo['title'])
            todo['description'] = data.get('description', todo['description'])
            return jsonify(todo)
    return jsonify({"error": "Todo not found"}), 404

# Delete a todo
@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todos
    new_todos = [todo for todo in todos if todo['id'] != todo_id]
    if len(new_todos) == len(todos):
        return jsonify({"error": "Todo not found"}), 404
    todos = new_todos
    return '', 204

# Mark as read
@app.route('/todos/<int:todo_id>/read', methods=['PATCH'])
def mark_as_read(todo_id):
    for todo in todos:
        if todo['id'] == todo_id:
            todo['read'] = True
            return jsonify(todo)
    return jsonify({"error": "Todo not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
