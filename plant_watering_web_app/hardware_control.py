import datetime
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)  # Broadcom pin-numbering scheme
water_sensor_pin = 8


def init_output(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    GPIO.output(pin, GPIO.HIGH)


def get_moisture_status(pin=8):

    GPIO.setup(pin, GPIO.IN)
    return GPIO.input(pin)


def pump_on(pump_pin=7, delay=1):
    init_output(pump_pin)
    with open('last_watered.txt', 'a') as f:
        f.write("Watered at {}\n".format(datetime.datetime.now().strftime("%d.%m.%Y, %H:%M:%S")))
    GPIO.output(pump_pin, GPIO.LOW)
    time.sleep(delay)
    GPIO.output(pump_pin, GPIO.HIGH)