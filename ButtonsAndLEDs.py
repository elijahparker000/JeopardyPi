from gpiozero import Button
from gpiozero import LED
from time import sleep
 

led1 = LED(2)
led2 = LED(3)
led3 = LED(4)
led4 = LED(17)
led5 = LED(27)

button1 = Button(22)
button2 = Button(10)
button3 = Button(9)
button4 = Button(11)
button5 = Button(5)

while True:
    if button1.is_pressed:
        led1.on()
    if button2.is_pressed:
        led2.on()
    if button3.is_pressed:
        led3.on()
    if button4.is_pressed:
        led4.on()
    if button5.is_pressed:
        led5.on()
    else:
        led1.off()
        led2.off()
        led3.off()
        led4.off()
        led5.off()