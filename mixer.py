import RPi.GPIO as GPIO
import time

port_out = [8,10,12,16,18]
port_in = [11,13]

def setup():
    GPIO.setmode(GPIO.BOARD)

    for p in port_out:
        GPIO.setup(p, GPIO.OUT)
        GPIO.output(p, GPIO.HIGH)

    for p in port_in:
        GPIO.setup(p, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

def run():
    while 1:
        if GPIO.input(11) == GPIO.HIGH:
            print("BoleroMalibu")
            boleromalibu()

        elif GPIO.input(13) == GPIO.HIGH:
            print("Bolero43")
            bolero43()
        time.sleep(1)

def bolero43():
    #43
    GPIO.output(8, GPIO.LOW)
    time.sleep(2)
    GPIO.output(8, GPIO.HIGH)

    #Maracuja
    GPIO.output(16, GPIO.LOW)
    time.sleep(4)
    GPIO.output(16, GPIO.HIGH)

    #Cranberry
    GPIO.output(18, GPIO.LOW)
    time.sleep(4)
    GPIO.output(18, GPIO.HIGH)

    #Limette
    GPIO.output(12, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(12, GPIO.HIGH)

def boleromalibu():
    #Malibu
    GPIO.output(10, GPIO.LOW)
    time.sleep(2)
    GPIO.output(10, GPIO.HIGH)

    #Maracuja
    GPIO.output(16, GPIO.LOW)
    time.sleep(4)
    GPIO.output(16, GPIO.HIGH)

    #Cranberry
    GPIO.output(18, GPIO.LOW)
    time.sleep(4)
    GPIO.output(18, GPIO.HIGH)

    #Limette
    GPIO.output(12, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(12, GPIO.HIGH)

setup()

run()
