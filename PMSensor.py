import serial # Imports the 'serial' module to enable communication with serial devices
import time   # Imports the 'time' module for handling delays

class PM25Sensor: # Defines a class named PM25Sensor to encapsulate sensor-related functionality
    def __init__(self, port='/dev/serial0', baudrate=9600, timeout=1):  # Initializes the sensor object with default port, baudrate, and timeout values
        self.ser = serial.Serial(port, baudrate=baudrate, timeout=timeout) # Opens a serial connection to the specified port with the given configuration

    def read_sensor_data(self):  # Defines a method to read data from the PM2.5 sensor
        request_frame = b'\x42\x4d\x00\x00\x00\x00\x00\x00\x00\x00' # Creates a byte array (request frame) to send to the sensor, initiating data retrieval
        self.ser.write(request_frame)  # Sends the request frame to the sensor
        time.sleep(1)   # Waits for 1 second to give the sensor time to respond

        data = self.ser.read(32)  # Reads 32 bytes of data from the sensor

        if len(data) == 32 and data[0] == 0x42 and data[1] == 0x4d:  # Checks if the received data is 32 bytes long and starts with 0x42 and 0x4d (valid header)
            pm2_5 = data[10] * 256 + data[11]  # PM2.5 Extracts and calculates the PM2.5 concentration value
            pm10 = data[12] * 256 + data[13]  # PM10 Extracts and calculates the PM10 concentration value
            return(f"PM2.5: {pm2_5} µg/m³, PM10: {pm10} µg/m³")  # Returns the PM2.5 and PM10 values in a formatted string
        else:
            print("error") # Prints an error message if data is invalid or improperly received

