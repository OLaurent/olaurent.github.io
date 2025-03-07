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



exercices = [
    {
        "id": str(uuid.uuid4()),
        "level": "Première",
        "theme": "Suites numériques",
        "selected" : False, 
        "content": r"""
        <p>Soit $(u_n)$ la suite définie pour $n \in \mathbb{N}$ par $u_n=-8 \times 0,9^n + 15$.</p>
        <ol>
            <li>Montrer que la suite $(u_n)$ est croissante.</li>
            <li>À l'aide de la calculatrice, déterminer le rang $n$ à partir duquel $u_n>14,5$.</li>
        </ol>
        """,
        "latexCode": r"""
                Soit $(u_n)$ la suite définie pour $n \in \N$ par $u_n=-8\times0,9^n+15$.
        \begin{enumerate}
        \item Montrer que la suite $(u_n)$ est croissante.
        \item \`A l'aide de la calculatrice, déterminer le rang $n$ à partir duquel $u_n>14,5$.
        \end{enumerate}"
        """
    },
    {
        "id": str(uuid.uuid4()),
        "level": "Première",
        "theme": "Suites numériques",
        "selected" : True, 
        "content": r"""
        <p>Soit $(v_n)$ la suite définie pour $n \in \mathbb{N}$ par $v_n=n^2-11n+10$.</p>
        <ol>
            <li>Montrer que $v_{n+1}-v_n=2n-10$.</li>
            <li>Résoudre l'inéquation $2n-10\geqslant 0$ et en déduire que la suite $(v_n)$ est monotone à partir d'un certain rang que l'on précisera.</li>
        </ol>
        """,
        "latexCode": r"""
        Soit $(v_n)$ la suite définie pour $n \in \N$ par $v_n=n^2-11n+10$.
        \begin{enumerate}
            \item Montrer que $v_{n+1}-v_n=2n-10$.
            \item Résoudre l'inéquation $2n-10\geqslant 0$ et en déduire que la suite $(v_n)$ est monotone à partir d'un certain rang que l'on précisera.
        \end{enumerate}
        """
    },
    {
        "id": str(uuid.uuid4()),
        "level": "Première",
        "theme": "Dérivation",
        "selected" : False, 
        "content": r"""
        <p>Un exercice bidon de dérivation.</p>
        """,
        "latexCode": r"""
        Un exercice bidon de dérivation.
        """
    }
]




@app.route('/')
def home():
    return render_template('index.html', todos=todos, exercices=exercices)

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


@app.route('/filter_exercices', methods=['GET'])
def filter_exercices():
    level = request.args.get('level')
    if level == 'all':
        return render_template('index.html', todos=todos, exercices=exercices)
    filtered_exercices = [exercice for exercice in exercices if exercice['level'] == level]
    return render_template('index.html', todos=todos, exercices=filtered_exercices)

if __name__ == '__main__':
    app.run(debug=True)