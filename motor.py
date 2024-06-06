# Lai varētu izmantot Raspberry pinus, importējam RPi.GPIO moduli
import RPi.GPIO as GPIO
from time import sleep

# Izvēlamies, kura numuru sistēma tiks izmantota (GPIO.BOARD vai GPIO.BCM)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class Motor():
    def __init__(self, ena, in1, in2):
        self.ena = ena
        self.in1 = in1
        self.in2 = in2
        GPIO.setup(self.ena, GPIO.OUT)
        GPIO.setup(self.in1, GPIO.OUT)
        GPIO.setup(self.in2, GPIO.OUT)
        
        # PWM (Pulse Width Modulation) - iespēja mainīt viļņa platumu, nemainot frekvenci, kas šajā gadījumā buus 100
        # t.i. motors griezīsies ātrāk vai lēnāk. Raspbery ir 4 pini, kas atbalsta PWM - GPIO12, ..13, ..18, ..19
        self.pwm = GPIO.PWM(self.ena, 100)
        self.pwm.start(0)

    def go(self, v=10, t=0):
        GPIO.output(self.in1,GPIO.LOW)  # GPIO.LOW = 0 vai '-'
        GPIO.output(self.in2,GPIO.HIGH) # GPIO.HIGH = 1 vai '+', samainot vietām, mainīsies griezšanās virziens (kā metodē revers)
        self.pwm.ChangeDutyCycle(v)  # griezšanās ātrums v
        print('go')
        sleep(t)
        
    def revers(self, v=10, t=0):
        GPIO.output(self.in1,GPIO.HIGH)
        GPIO.output(self.in2,GPIO.LOW)
        print('revers')
        self.pwm.ChangeDutyCycle(v)
        sleep(t)
        
    def stops(self, t=0):
        self.pwm.ChangeDutyCycle(0)
        print('stop')
        sleep(t)
    
