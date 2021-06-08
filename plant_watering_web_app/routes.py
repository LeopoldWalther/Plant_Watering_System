import datetime
import psutil
import os
from flask import render_template

from plant_watering_web_app import app
from .hardware_control import PlantWateringSystem

plant_watering_system = PlantWateringSystem()


def message_template(text=""):
    current_time = datetime.datetime.now().strftime("%d.%m.%Y, %H:%M:%S")
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


@app.route("/sensor")
def check_humidity():
    is_humid = plant_watering_system.get_moisture_status()
    if is_humid:
        text = "I'm a happy plant"
    else:
        text = "Plant is dry, please water!"

    message = message_template(text=text)
    return render_template('dashboard.html', **message)


@app.route("/water_once")
def pump_water():
    plant_watering_system.pump_once()
    message = message_template(text="Watered Once")
    return render_template('dashboard.html', **message)


@app.route("/auto/water/<toggle>")
def auto_water(toggle):
    """
    running = False
    if toggle == "ON":
        message = message_template(text="Auto Watering On")
        for process in psutil.process_iter():
            try:
                if process.cmdline()[1] == 'auto_water.py':
                    message = message_template(text="Already Running!")
                    running = True
            except:
                pass
        if not running:
            os.system("python3 auto_water.py&")

    else:
        message = message_template(text="Auto Watering Off")
        os.system("pkill -f hardware_control.py")
    """
    message = message_template(text="Auto Watering Function currently out of Service")

    return render_template('dashboard.html', **message)
