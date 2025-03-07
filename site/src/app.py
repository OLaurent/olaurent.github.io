from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///exercices.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key'  # Nécessaire pour utiliser flash messages
db = SQLAlchemy(app)

from models import Exercice

@app.route('/')
def home():
    exercices = Exercice.query.all()
    return render_template('index.html', exercices=exercices)

@app.route('/edit_exercise', methods=['GET', 'POST'])
def edit_exercise():
    if request.method == 'POST':
        # Traitement du formulaire
        exercice_id = request.form.get('id')
        exercice = Exercice.query.get(exercice_id)
        if exercice is None:
            print('Exercice non trouvé.')
            return redirect(url_for('home'))

        exercice.level = request.form.get('level')
        exercice.theme = request.form.get('theme')
        exercice.content = request.form.get('content')
        exercice.latex_code = request.form.get('latex_code')
        exercice.correction = request.form.get('correction')
        exercice.latex_correction = request.form.get('latex_correction')
        db.session.commit()
        flash('Exercice mis à jour avec succès.', 'success')
        return redirect(url_for('home'))
    else:
        exercice_id = request.args.get('id')
        exercice = Exercice.query.get(exercice_id)
        if exercice is None:
            flash('Exercice non trouvé.', 'error')
            return redirect(url_for('home'))
        return render_template('edit_exercise.html', exercice=exercice)

if __name__ == '__main__':
    app.run(debug=True)