import RPi.GPIO as GPIO
import time

#calibrate Servo min max and offset
OFFSE_DUTY = -0.50
SERVO_MIN_DUTY = 2.5+OFFSE_DUTY
SERVO_MAX_DUTY = 12.5+OFFSE_DUTY
servoPin = 12

def map( value, fromLow, fromHigh, toLow, toHigh):  # map a value from one range to another range
    return (toHigh-toLow)*(value-fromLow) / (fromHigh-fromLow) + toLow

def setup():
    global p
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(servoPin, GPIO.OUT)
    GPIO.output(servoPin, GPIO.LOW)
    #PWM freq
    p = GPIO.PWM(servoPin, 50)
    p.start(0)

def servoWrite(angle):
    #rotate servo to specific angle, 0-180
    if(angle<0):
        angle = 0
    elif(angle > 180):
        angle = 180
    p.ChangeDutyCycle(map(angle,0,180,SERVO_MIN_DUTY,SERVO_MAX_DUTY))

def open():
 for dc in range(0,91,1):
  servoWrite(dc)
  time.sleep(0.01)
  #print(dc)

def close():
 for dc in range(90,-1,-1):
  servoWrite(dc)
  time.sleep(0.01)
  #print(dc)

def destroy():
    p.stop()
#    GPIO.cleanup()

"""
print ('Program is starting...')
setup()
servoWrite(0)
time.sleep(1)
open()
time.sleep(5)
close()
destroy()
"""
