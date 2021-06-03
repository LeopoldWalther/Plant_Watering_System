from flask import Flask

app = Flask(__name__)

from plant_watering_web_app import routes
