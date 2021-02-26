import RPi.GPIO as GPIO
import time
import random

#define gpio pins
pins = [11, 13]

def setup():
    global pwmRed,pwmGreen
    #setup with GPIO board numbering
    GPIO.setmode(GPIO.BOARD)
    #set pins to output mode on high level
    GPIO.setup(pins, GPIO.OUT)
    GPIO.output(pins, GPIO.HIGH)
    #set PWM frequency to 2000 Hz
    pwmRed = GPIO.PWM(pins[1], 2000)
    pwmGreen = GPIO.PWM(pins[0], 2000)
    pwmRed.start(0)
    pwmGreen.start(0)


def setColor(r_val,g_val):
    #change duty cycle
    pwmRed.ChangeDutyCycle(r_val)
    pwmGreen.ChangeDutyCycle(g_val)

def destroy():
    pwmRed.stop()
    pwmGreen.stop()
    GPIO.cleanup()

