from flask import Blueprint, render_template, request
from .models import db, Exercice

routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
    exercices = Exercice.query.all()
    return render_template('index.html', exercices=exercices)

@routes.route('/filter_exercices', methods=['GET'])
def filter_exercices():
    level = request.args.get('level')
    if level == 'all':
        exercices = Exercice.query.all()
    else:
        exercices = Exercice.query.filter_by(level=level).all()
    return render_template('index.html', exercices=exercices)