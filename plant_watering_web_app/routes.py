from plant_watering_web_app import app
import json
import plotly
from flask import render_template


@app.route('/')
def index():
    return "Leo will control his plant watering system from all over the world with this web app!"


@app.route('/control-center.html')
def control_center():
    message = 'Hello World'
    return render_template('control-center.html', message=message)

