import datetime
import time
import RPi.GPIO as GPIO


class PlantWateringSystem(object):

    def __init__(self):
        GPIO.setmode(GPIO.BOARD)  # Broadcom pin-numbering scheme
        self.water_sensor_pin = 8
        self.pump_pin = 7
        self.is_humid = False

    def init_output(self, pin):
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)
        GPIO.output(pin, GPIO.HIGH)

    def get_moisture_status(self):
        """Checks if moisture sensor measures humidity"""
        with open('log.csv', 'a') as f:
            f.write("checked humidity, {};\n".format(datetime.datetime.now().strftime("%d.%m.%Y, %H:%M:%S")))
            GPIO.setup(self.water_sensor_pin, GPIO.IN)
            if GPIO.input(self.water_sensor_pin) == 0:
                self.is_humid = True
                log_entry = "plant measured humid, {};\n".format(datetime.datetime.now().strftime("%d.%m.%Y, %H:%M:%S"))
            else:
                self.is_humid = False
                log_entry = "plant measured dry, {};\n".format(datetime.datetime.now().strftime("%d.%m.%Y, %H:%M:%S"))

            f.write(log_entry)
        return self.is_humid

    def auto_water(self, delay=5):
        consecutive_water_count = 0
        self.init_output(self.pump_pin)
        try:
            while consecutive_water_count < 10:
                time.sleep(delay)
                wet = self.get_moisture_status()
                if not wet:
                    if consecutive_water_count < 5:
                        self.pump_on()
                    consecutive_water_count += 1
                else:
                    consecutive_water_count = 0
        except KeyboardInterrupt:  # If CTRL+C is pressed, exit cleanly:
            print('Exception:')
            GPIO.cleanup()  # cleanup all GPI

    def pump_on(self, delay=1):
        self.init_output(self.pump_pin)

        with open('log.csv', 'a') as f:
            f.write("watered, {};\n".format(datetime.datetime.now().strftime("%d.%m.%Y, %H:%M:%S")))

        GPIO.output(self.pump_pin, GPIO.LOW)
        time.sleep(delay)
        GPIO.output(self.pump_pin, GPIO.HIGH)
