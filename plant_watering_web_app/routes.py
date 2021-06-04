from plant_watering_web_app import app
import json
import plotly
from flask import render_template


@app.route('/')
def index():
    message = 'Leo will control his plant watering system from all over the world with this web app!'
    return render_template('dashboard.html', message=message)


@app.route('/cakes')
def cakes():
    return 'Yummy cakes!'
