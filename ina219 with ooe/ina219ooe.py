from machine import I2C, Pin
from ina219 import INA219
from time import sleep
import utime


class InaMod:
    def __init__(self):
        # I2C Initialization (SDA: GP0, SCL: GP1)
        self.i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)

        # INA219-Sensor Initialization
        self.ina = INA219(self.i2c)
        self.ina.set_calibration_32V_1A()



    def scan(self):
        # I2C-Scan - searching for connected Devices on the I2C Bus
        self.devices = self.i2c.scan()
        if self.devices:
            print("I2C devices found:", [hex(device) for device in self.devices])
        else:
            print("No I2C devices found. Check connections!")
            while True:
                pass



    def status(self):
        self.current = self.ina.current
        if self.current <= 0.05:
            self.current = 0
            
        self.voltage = self.ina.bus_voltage
        if self.voltage <= 0.05:
            self.voltage = 0
            
        return self.current, self.voltage



    def inaprint(self, current, voltage):
        print("{:.2f} mA  {:.2f} V".format(current, voltage))


ina = InaMod()

def main():
    ina.scan()
    while True:
        current, voltage = ina.status()
        ina.inaprint(current, voltage)
        utime.sleep_ms(250)




if __name__ == "__main__":
    main()
    

