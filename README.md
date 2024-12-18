# Sensor Integrations: BME280 & LTR390
This repository provides integration for two widely used environmental sensors: BME280 and LTR390. These sensors can be used to measure environmental parameters such as temperature, humidity, pressure, and UV light intensity.

## BME280
The BME280 is a highly accurate sensor from Bosch that combines a temperature, humidity, and pressure sensor in a single compact device. It's perfect for a variety of applications, including weather stations, climate monitoring, and IoT projects. The sensor communicates with microcontrollers over I2C or SPI interfaces and provides high-resolution data that can be used for environmental sensing in embedded systems.

### Key Features:

Temperature: ±1°C
Humidity: ±3% RH
Pressure: ±1 hPa

Low power consumption
I2C & SPI interface

*******************************************************************************
## LTR390
The LTR390 is a precision UV light sensor from LITE-ON, designed to measure ultraviolet (UV) light intensity in the 200–400nm range. This sensor is especially useful in applications like UV index monitoring, outdoor environmental monitoring, and wearable health devices. The LTR390 is capable of high-speed measurements with low power consumption, making it ideal for portable devices.

### Key Features:

Measures UV light intensity (200–400nm)
High accuracy and low power consumption
I2C interface for easy integration
Wide dynamic range

*******************************************************************************
### MP2.5 5003 Sensor
The MP2.5 5003 is a reliable particulate matter sensor designed for detecting PM2.5 particles in the air using laser scattering technology. It is compact, energy-efficient, and ideal for air quality monitoring, IoT systems, and environmental projects. The sensor provides accurate, real-time data and supports easy integration into embedded systems through standard communication protocols.

### Key Features:
PM2.5 Detection: High accuracy and real-time monitoring
Compact Design: Lightweight and easy to integrate
Low Power Consumption: Suitable for IoT and portable devices
Communication Interface: UART and other standard protocols

********************************************************************************

# Which file for what:

***bme280Sensor.py*** code in python which read information from sensor bme280

***ltr390Sensor.py*** Code in python which read infotmation from sensor ltr390

***PMSensor.py*** Code in python which read infotmation from sensor MP2.5

***main.py***  main file wich run the porgrame and return results

***reuarement.tet*** .txt file wich contain all needed librarys


********************************************************************************
> [!TIP]
> Helpful advice for doing things better or more easily.

How to run the code:


Step 1: Creat virtual environment

    python3 -m venv [name_of_your_environment]

Step 2: Enter in environment

    source [name_of_your_environement]/bin/activate

Step 3: Install all needed lybrarys 

    pip install -r requirements.txt

Step 4: Run the Programm 
 
    python3 main.py

Step 5: Deactivate environement 

    deactivate
