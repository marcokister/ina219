from ina219ooe import InaMod
import utime

ina = InaMod()



def main():
    ina.scan()
    while True:
        current, voltage = ina.status()
        ina.inaprint(current, voltage)
        utime.sleep_ms(250)



if __name__ == "__main__":
    main()