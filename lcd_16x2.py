from machine import Pin, SoftI2C
from time import sleep
from lcd_i2c import LCD

i2c_addr = 0x27
row = 2
column = 16

i2c = SoftI2C(scl=Pin(22), sda=(21))
lcd = LCD(addr=i2c_addr, cols=column, rows=row, i2c=i2c)

while True:
    lcd.begin()
    lcd.clear()
    lcd.set_cursor(2, 0)
    lcd.print("Hello World!")
    sleep(0.5)
    lcd.clear()
    lcd.set_cursor(2, 1)
    lcd.print("Hello World!")
    sleep(0.5)
    


