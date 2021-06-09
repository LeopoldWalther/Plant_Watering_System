import datetime
import time
import RPi.GPIO as GPIO


class PlantWateringSystem(object):

    def __init__(self):
        GPIO.setmode(GPIO.BOARD)  # Broadcom pin-numbering scheme
        self.high_runner_moisture_sensor_pin = 8
        self.low_runner_moisture_sensor_pin = 10
        self.high_runner_pump_pin = 7
        self.low_runner_pump_pin = 17
        self.is_humid = False

    def get_moisture_status(self, moisture_sensor):
        """Checks if moisture sensor measures humidity"""
        if moisture_sensor == 'high_runner':
            moisture_sensor_pin = self.high_runner_moisture_sensor_pin
        else:
            moisture_sensor_pin = self.low_runner_moisture_sensor_pin

        with open('log.csv', 'a') as f:
            f.write("checked {} humidity, {};\n".format(
                moisture_sensor, datetime.datetime.now().strftime("%d.%m.%Y, %H:%M:%S")))

            GPIO.setup(moisture_sensor_pin, GPIO.IN)
            moisture_sensor_status = GPIO.input(moisture_sensor_pin)

            if moisture_sensor_status == 0:
                self.is_humid = True
                log_entry = "{} measured humid, {};\n".format(
                    moisture_sensor, datetime.datetime.now().strftime("%d.%m.%Y, %H:%M:%S"))
            else:
                self.is_humid = False
                log_entry = "{} measured dry, {};\n".format(
                    moisture_sensor, datetime.datetime.now().strftime("%d.%m.%Y, %H:%M:%S"))

            f.write(log_entry)
        return self.is_humid

    def auto_water(self, delay=5):
        """
        consecutive_water_count = 0
        self.init_output(pump_pin)
        print("Here we go! Press CTRL+C to exit")
        try:
            while 1 and consecutive_water_count < 10:
                time.sleep(delay)
                wet = self.get_moisture_status()
                if not wet:
                    if consecutive_water_count < 5:
                        self.pump_on()
                    consecutive_water_count += 1
                else:
                    consecutive_water_count = 0
        except KeyboardInterrupt:  # If CTRL+C is pressed, exit cleanly:
            GPIO.cleanup()  # cleanup all GPI

    """

    def pump_once(self, pump, delay=1):

        if pump == 'high_runner':
            pump_pin = self.high_runner_pump_pin
        else:
            pump_pin = self.low_runner_pump_pin

        GPIO.setup(pump_pin, GPIO.OUT)
        GPIO.output(pump_pin, GPIO.LOW)

        with open('log.csv', 'a') as f:
            f.write("{} watered, {};\n".format(pump, datetime.datetime.now().strftime("%d.%m.%Y, %H:%M:%S")))

        GPIO.output(pump_pin, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(pump_pin, GPIO.LOW)
