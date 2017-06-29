from gpiozero import LED, Button
from time import time, sleep
from random import randint

led = LED(17)
btn = Button(10)


while True:
    sleep(randint(0,10))
    led.on()
    start = time()
    btn.wait_for_press()
    led.off()
    end = time()
    print(end-start)
