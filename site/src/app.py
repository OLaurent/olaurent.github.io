from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///exercices.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Exercice

@app.route('/')
def home():
    exercices = Exercice.query.all()
    return render_template('index.html', exercices=exercices)

if __name__ == '__main__':
    app.run(debug=True)