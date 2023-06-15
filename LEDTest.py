import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
led_pin = 20
GPIO.setup(led_pin, GPIO.OUT)

while(True):
    GPIO.output(led_pin, GPIO.HIGH)
    time.sleep(0.5)

    GPIO.output(led_pin, GPIO.LOW)
    time.sleep(0.5)
