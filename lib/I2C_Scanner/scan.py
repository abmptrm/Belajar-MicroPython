from machine import Pin, SoftI2C
from time import sleep

i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
addr = i2c.scan()

while True:
    if addr == []:
        print("I2C Tidak Terdeteksi !")
    else :
        print("I2C Terdeteksi !")
        print(str(addr) + " => " + hex(addr[0]))
    sleep(2.0)
    


