from machine import I2C, Pin
from ina219 import INA219
from time import sleep
from ssd1306 import SSD1306_I2C
import utime

# I2C initialisieren (SDA: GP0, SCL: GP1)
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)

# I2C-Scan durchführen
devices = i2c.scan()
if devices:
    print("I2C devices found:", [hex(device) for device in devices])
else:
    print("No I2C devices found. Check connections!")
    while True:
        pass


def oled_output(voltage):
    oled.fill(0)
    oled.text(f"Voltage: {voltage:.2f}V", 1, 24)
    oled.show()


# INA219-Sensor initialisieren
ina = INA219(i2c)

# Alternativ: 32V und 1A Kalibrierung
ina.set_calibration_32V_1A()

# Endlosschleife
while True:
    try:
        current = ina.current
        voltage = ina.bus_voltage
        if current < 0:
            current = 0
            
        print("{:.2f} mA  {:.2f} V".format(current, voltage))
        oled_output(voltage)
        utime.sleep_ms(250)
    except Exception as e:
        print("Error reading INA219:", e)
    sleep(1)
