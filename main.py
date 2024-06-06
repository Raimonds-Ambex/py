# v1
# Raspberry Pi projekts - robots, kas pabrauc nost, ja notiek ar kustību sensoru konstatēta kustība
# Lai nākotnē varētu izmantot vairāk sensorus, tie tiks sadalīti pa kodoliem

from gpiozero import MotionSensor
import threading
from time import sleep
import motor

import multiprocessing
cores = multiprocessing.cpu_count()
print("Kodolu skaits = %d" % cores)  # noskaidrojam kodolu skaitu

pir = MotionSensor(16)
motor1 = motor.Motor(13,3,4)

def first_loop(v,t,s):
    while True:
        pir.wait_for_motion()
        motor1.go(v,t) # ātrums, laiks
        motor1.stops(s)  # laiks

        pir.wait_for_no_motion()
   
def second_loop():
    while True:
        print('Šis būs kodols distances sensoram')  # pagaidām vēl nav
        sleep(20)


t1 = threading.Thread(target = first_loop, args=(77, 1, 9))  # thread t1 pirmajam kodolam
t2 = threading.Thread(target = second_loop)  # thread otrajam kodolam

t1.start()
t2.start()
# t2.join()

# print('End')