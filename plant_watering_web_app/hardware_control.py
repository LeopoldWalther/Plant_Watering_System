import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)  # Broadcom pin-numbering scheme

water_sensor_pin = 8


def get_moisture_status(pin=8):
    GPIO.setup(pin, GPIO.IN)
    return GPIO.input(pin)