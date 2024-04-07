from machine import Pin, SoftI2C
from i2c_lcd import LCD_I2C
from time import sleep

led = Pin(2, Pin.OUT)

i2c = SoftI2C(scl=Pin(21), sda=Pin(22))
lcd = LCD_I2C(16, 2, i2c, addr=0x27)


while True:
    lcd.text("HELLO 1", 0, 0)
    lcd.text("HELLO 2", 1, 20)
    lcd.show()
    
        
        
   
    