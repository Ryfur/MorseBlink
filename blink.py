from gpiozero import LED
from time import sleep
from random import uniform

red = LED(17)


while True:
    time = uniform(0.01,1)
    red.blink(time,time,10)
    print("Blink lasts {0:.2f} seconds!".format(time))
    sleep(time*2*10)
