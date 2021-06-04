from plant_watering_web_app import app
import datetime
import json
import plotly
from flask import render_template
from .hardware_control import  get_moisture_status


def message_template(text=""):
    current_time = datetime.datetime.now().strftime("%d.%m-%Y, %H:%M:%S")
    message = {
        'time': current_time,
        'text': text
    }
    return message


@app.route('/')
@app.route('/index')
def index():
    message = message_template()
    return render_template('dashboard.html', **message)


@app.route('/cakes')
def cakes():
    return 'Yummy cakes!'


@app.route("/sensor")
def is_wet():
    status = get_moisture_status()
    text = ""

    if status == 1:
        text = "Water me please!"
    else:
        text = "I'm a happy plant"

    message = message_template(text=text)
    return render_template('dashboard.html', **message)


@app.route("/auto/water/<toggle>")
def auto_water(toggle):
    running = False
    if toggle == "ON":
        message = message_template(text="Auto Watering On")
        """
        for process in psutil.process_iter():
            try:
                if process.cmdline()[1] == 'auto_water.py':
                    message = message_template(text ="Already running")
                    running = True
            except:
                pass
        if not running:
            os.system("python3.4 auto_water.py&")
        """
    else:
        message = message_template(text="Auto Watering Off")

        """
        os.system("pkill -f water.py")
        """

    return render_template('dashboard.html', **message)
