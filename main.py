from machine import I2C, Pin
from ina219 import INA219
from time import sleep
import utime

# I2C Initialization (SDA: GP0, SCL: GP1)
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)

# I2C-Scan - searching for connected Devices on the I2C Bus
devices = i2c.scan()
if devices:
    print("I2C devices found:", [hex(device) for device in devices])
else:
    print("No I2C devices found. Check connections!")
    while True:
        pass


# INA219-Sensor Initialization
ina = INA219(i2c)
ina.set_calibration_32V_1A()

# main loop
while True:
    try:
        current = ina.current
        voltage = ina.bus_voltage
        
        if current <= 0.05:
            current = 0
            
        if voltage <= 0.05:
            voltage = 0
            
        print("{:.2f} mA  {:.2f} V".format(current, voltage))
        utime.sleep_ms(250)
        
    except Exception as e:
        print("Error reading INA219:", e)
        
    sleep(1)

