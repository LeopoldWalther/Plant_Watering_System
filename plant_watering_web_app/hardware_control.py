import datetime
import time
import RPi.GPIO as GPIO


class PlantWateringSystem(object):

    def __init__(self):
        GPIO.setmode(GPIO.BOARD)  # Broadcom pin-numbering scheme
        self.high_runner_moisture_sensor_pin = 8
        self.low_runner_moisture_sensor_pin = 10
        self.high_runner_pump_pin = 7
        self.low_runner_pump_pin = 29
        self.is_humid = False

    def get_moisture_status(self, plant_circuit):
        """Checks if moisture sensor measures humidity"""
        if plant_circuit == 'high_runners':
            moisture_sensor_pin = self.high_runner_moisture_sensor_pin
        elif plant_circuit == 'low_runners':
            moisture_sensor_pin = self.low_runner_moisture_sensor_pin
        else:
            moisture_sensor_pin = -1

        with open('log.csv', 'a') as f:
            f.write("checked {} humidity, {};\n".format(
                plant_circuit, datetime.datetime.now().strftime("%d.%m.%Y, %H:%M:%S")))

            GPIO.setup(moisture_sensor_pin, GPIO.IN)
            moisture_sensor_status = GPIO.input(moisture_sensor_pin)

            if moisture_sensor_status == 0:
                self.is_humid = True
                log_entry = "{} measured humid, {};\n".format(
                    plant_circuit, datetime.datetime.now().strftime("%d.%m.%Y, %H:%M:%S"))
            else:
                self.is_humid = False
                log_entry = "{} measured dry, {};\n".format(
                    plant_circuit, datetime.datetime.now().strftime("%d.%m.%Y, %H:%M:%S"))

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

    def pump_once(self, plant_circuit, delay=1):

        if plant_circuit == 'high_runners':
            pump_pin = self.high_runner_pump_pin
        elif plant_circuit == 'low_runners':
            pump_pin = self.low_runner_pump_pin
        else:
            pump_pin = -1

        GPIO.setup(pump_pin, GPIO.OUT)
        GPIO.output(pump_pin, GPIO.LOW)

        with open('log.csv', 'a') as f:
            f.write("{} watered, {};\n".format(plant_circuit, datetime.datetime.now().strftime("%d.%m.%Y, %H:%M:%S")))

        GPIO.output(pump_pin, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(pump_pin, GPIO.LOW)
