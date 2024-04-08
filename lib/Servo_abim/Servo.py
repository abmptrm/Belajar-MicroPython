# github.com/abmptrm

class Servo:
    def __init__(self, pin, angle, in_min, in_max, out_min, out_max):
        self.pin = pin
        self.angel = angle
        self.in_min = 0
        self.in_max = 180
        self.out_min = 20
        self.out_max = 120
        
    def servo_formula(self, angle, in_min, in_max, out_min, out_max):
        return int((self.angle - self.in_min) * (self.out_max - self.out_min) / (self.in_max - self.in_min) + self.out_min)
    
    def write_servo(self, pin, angle, in_min, in_max, out_min, out_max):
        self.pin.duty(servo_formula(self.angle, self.in_min, self.in_max, self_out_min, self.out_max))