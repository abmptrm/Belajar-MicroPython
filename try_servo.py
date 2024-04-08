from Servo import Servo
from machine import Pin, PWM
from time import sleep

# init pin and pwm
pin23 = Pin(23, Pin.OUT)
pwm23 = PWM(pin23)

# init value freq = 50 (min freq = 40)
pwm23.freq(50)

# init duty cycle = 0
pwm23.duty(0)

Servo.write_servo(pwm, 180)


# To rotate the servo from 0 to 180 degrees
# by 10 degrees decrement
for i in range(0, 181, 10):
    servo(pwm, i)
    time.sleep(0.5)
    
# To rotate the servo from 180 to 0 degrees
# by 10 degrees decrement
for i in range(180, -1, -10):
    servo(pwm, i)
    time.sleep(0.5)




