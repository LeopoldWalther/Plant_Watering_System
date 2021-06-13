import datetime
import pytz
from flask import render_template

from plant_watering_web_app import app
from .hardware_control import PlantWateringSystem

plant_watering_system = PlantWateringSystem()


def message_template(text=""):
    current_time = datetime.datetime.now()

    local_timezone = pytz.timezone('Europe/Berlin')
    current_time_berlin = local_timezone.localize(current_time)

    message = {
        'time': current_time_berlin.strftime("%d.%m.%Y, %H:%M:%S"),
        'text': text
    }
    return message


@app.route('/')
@app.route('/index')
def index():
    message = message_template()
    return render_template('dashboard.html', **message)


@app.route("/sensor/<plants>")
def check_humidity(plants):
    print(plants)
    is_humid = plant_watering_system.get_moisture_status(plants)
    if is_humid:
        text = "{}s wet!".format(plants)
    else:
        text = "{}s dry, please water!".format(plants)

    message = message_template(text=text)
    return render_template('dashboard.html', **message)


@app.route("/water/<plants>")
def pump_water(plants):
    print(plants)
    plant_watering_system.pump_once(plants)
    text = 'Watered {} plants'.format(plants)
    message = message_template(text=text)
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
    message = message_template(text="Auto Watering Function \ncurrently out of Service")

    return render_template('dashboard.html', **message)
