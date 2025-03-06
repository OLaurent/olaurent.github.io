from flask import Flask, render_template, redirect, request
import uuid

app = Flask(__name__)
app.debug = True

todos = [
    {
        "id": str(uuid.uuid4()),
        "title": "Complete project report",
        "done": False
    },
    {
        "id": str(uuid.uuid4()),
        "title": "Buy groceries",
        "done": False
    },
    {
        "id": str(uuid.uuid4()),
        "title": "Schedule dentist appointment",
        "done": False
    },
    {
        "id": str(uuid.uuid4()),
        "title": "Prepare for presentation",
        "done": False
    },
    {
        "id": str(uuid.uuid4()),
        "title": "Read a book",
        "done": False
    }
]

@app.route('/')
def home():
    return render_template('index.html', todos=todos)

@app.route('/create_todo', methods=['POST'])
def create_todo():
    title = request.form['title']
    todos.append({
        "id": str(uuid.uuid4()),
        "title": title,
        "done": False
    })
    return redirect('/')

@app.route('/update_todo/<string:id>')
def update_todo(id):
    global todos
    for todo in todos:
        if todo['id'] == id:
            todo['done'] = not todo['done']
    return redirect('/')

@app.route('/delete_todo/<string:id>')
def delete_todo(id):
    global todos
    todos = [todo for todo in todos if todo['id'] != id]
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)