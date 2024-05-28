# Lai varētu izmantot Raspberry pinus, importējam RPi.GPIO moduli
import RPi.GPIO as GPIO 
from time import sleep

# Izvēlamies, kura numuru sistēma tiks izmantota (GPIO.BOARD vai GPIO.BCM)
GPIO.setmode(GPIO.BCM)

# GPIO.setwarnings(False)
class Motor():
    def __init__(self, Ena, In1, In2):
        self.Ena = Ena
        self.In1 = In1
        self.In2 = In2
        GPIO.setup(self.Ena, GPIO.OUT)
        GPIO.setup(self.In1, GPIO.OUT)
        GPIO.setup(self.In2, GPIO.OUT)
        # PWM (Pulse Width Modulation) - iespēja mainīt viļņa platumu, nemainot frekvenci, kas šajā gadījumā buus 100
        # t.i. motors griezīsies ātrāk vai lēnāk. Raspbery ir 4 pini, kas atbalsta PWM - GPIO12, ..13, ..18, ..19
        self.pwm = GPIO.PWM(self.Ena, 100)
        self.pwm.start(0)

    def moveF(self, x=50, t=0):
        GPIO.outpoot(self.In1,GPIO.LOW)
        GPIO.outpoot(self.In2,GPIO.HIGH)
        self.pwm.ChangeDutyCycle(x)
        sleep(t)
    
    def stop(self, t=0)
        self.pwm.ChangeDutyCycle(x)
        sleep(t)

motor1 = Motor(2, 3, 4)
motor2 = Motor(17, 22, 25)

while True:
    motor1.moveF(30,2)
    motor1.stop(2)
