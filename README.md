# INA219 Raspberry Pi Pico with MicroPython Code for Measuring Voltage and Current 9-32V

### !!! FIND more Information on https://kiscando.de/strom-und-spannung-messen-mit-dem-ina219-am-raspberry-pi-pico-w-und-micropython/ ###
### only in german available ###

## Overview
This project provides a MicroPython code implementation for the Raspberry Pi Pico to measure voltage and current using an INA219 sensor module. It is designed as a simple and effective example for real-time monitoring of electrical parameters in embedded applications.

## Features
- **Real-Time Measurement:** Continuously monitors voltage and current.
- **Minimal Hardware Setup:** Requires only the Raspberry Pi Pico and an INA219 sensor module.
- **Educational Value:** A practical example to learn about sensor interfacing with MicroPython on the Raspberry Pi Pico.

## Hardware Requirements
- **Raspberry Pi Pico** Recommend Raspberry Pi Pico 2 W (W = with wlan)
- **INA219 Sensor Module** (or a compatible voltage/current sensor)
- Jumper wires
- Breadboard (optional, for prototyping)
- USB cable for power and programming

## Software Requirements
- **MicroPython Firmware** for the Raspberry Pi Pico  
  [Download here](https://micropython.org/download/rp2-pico/)
- **Thonny IDE** (or any compatible MicroPython editor) (Pytohn Interpreter is included in Thonny)
  [Download Thonny](https://thonny.org/)


## Installation

1. **Flash MicroPython Firmware:**  
   Follow the official [MicroPython guide for the Raspberry Pi Pico](https://docs.micropython.org/en/latest/rp2/quickref.html) to flash the firmware onto your Pico.

2. **Connect the Sensor:**  
   Wire the INA219 sensor to the Pico as follows:
   - **SDA:** Connect to the Pico's I2C SDA pin GP0
   - **SCL:** Connect to the Pico's I2C SCL pin GP1
   - **Power:** Ensure the sensor is powered with the appropriate voltage (3.3V or 5V depending on the module specifications).
   
   *(Look into my wiring diagramm)

3. **Clone or Download the Repository:**  
   Use Git to clone the repository or download it as a ZIP file from GitHub.
   Use my special ina219.py Module only for Raspberry Pi Pico / Pico 2 / 2W
   ssd1306.py is specially for Raspberry Pi Pico / Pico 2 / 2W to connect an oled I2C Display

4. **Wiring
   Connect + from external power supply (battery e.g.) with VIN+ on the INA219 Module
   Connect - from external power supply (battery e.g.) with GND Raspbery Pi Pico or GND on INA219 Module
   for only voltage measurement there is NO connection from VIN- to something!
   ATTENTION: VIN+ is for + from external power supply / battery
   ATTENTION: VIN- is NOT for connection to - from external power supply / battery !!!!
   INFO: if you want to meausure current and voltage you have to wire a device like engine or lamp e.g on VIN- to + from device and from - Device to - external power supply / battery

5. **You can find more information about the project on my blog** (only in german available)
   [www.kiscando.de](https://kiscando.de/strom-und-spannung-messen-mit-dem-ina219-am-raspberry-pi-pico-w-und-micropython/)


#####################################
## Disclaimer / Haftungsausschluss ##
#####################################

### English
**Warning:** Working with electronics involves inherent risks. You must ensure that you have the proper knowledge, skills, and precautions before attempting any modifications or experiments. The project owner and contributors assume no responsibility for any damage, injury, or loss resulting from the use or misuse of this project. Always exercise caution and follow safety guidelines when working with electronic components.

### Deutsch
**Achtung:** Die Arbeit mit Elektronik birgt inhärente Risiken. Du musst sicherstellen, dass du über das nötige Wissen, die erforderlichen Fähigkeiten und Vorsichtsmaßnahmen verfügst, bevor du Änderungen vornimmst oder Experimente durchführst. Der Projektinhaber und die Mitwirkenden übernehmen keine Verantwortung für Schäden, Verletzungen oder Verluste, die durch die Nutzung oder den Missbrauch dieses Projekts entstehen. Übe stets Vorsicht und folge den Sicherheitsrichtlinien beim Arbeiten mit elektronischen Komponenten.
