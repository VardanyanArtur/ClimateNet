import board # Provides access to the board's hardware (I2C pins, etc.)
import time  # Imports the 'time' module, though it's not directly used in this script
from adafruit_bme280 import basic as adafruit_bme280 # Imports the library for the BME280 sensor

class BME280:   # Defines a class named BME280 to manage the BME280 sensor
    def __init__(self): # Initializes the sensor object
        self.i2c = board.I2C() # Sets up I2C communication using default SCL and SDA pins
        self.bme280 = adafruit_bme280.Adafruit_BME280_I2C(self.i2c, 0x76) # Connects to the BME280 sensor at I2C address 0x76
 
    def read_bme_data(self):   # Defines a method to get data from the BME280 sensor
        return self.bme280.temperature, self.bme280.relative_humidity, self.bme280.pressure  # Returns temperature, humidity, and pressure readings from the sensor


