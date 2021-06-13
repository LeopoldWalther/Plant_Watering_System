#!/bin/bash

source /home/pi/Documents/Projects/PlantWateringSystem/Plant_Watering_System/env380/bin/activate && python3 plant_watering_web_app.py &

alias env380="source $HOME/pi/Documents/Projects/PlantWateringSystem/Plant_Watering_System/env380/bin/activate"