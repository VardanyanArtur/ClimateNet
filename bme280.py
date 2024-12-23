import time  # Imports the 'time' module, though it's not actively used in this script
import board  # Provides access to the board's hardware (I2C pins, etc.)
import adafruit_ltr390  # Imports the library for the LTR390 sensor

class LTR390: # Defines a class named LTR390 to manage the LTR390 sensor
    def __init__(self):  # Initializes the sensor object
        self.i2c = board.I2C()  # uses board.SCL and board.SDA # Sets up I2C communication using default SCL and SDA pins
        self.ltr = adafruit_ltr390.LTR390(self.i2c, 0x53)  # Connects to the LTR390 sensor at I2C address 0x53

    def read_ltr_data(self):  # Defines a method to get data from the LTR390 sensor
        return self.ltr.uvi, self.ltr.light # Returns the UV Index (uvi) and light intensity (light) measured by the sensor


