import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
switch1=35
switch2=37
motor1=38
motor2=40
GPIO.setmode(GPIO.BOARD)
GPIO.setup(switch1,GPIO.IN,GPIO.PUD_UP)
GPIO.setup(switch2,GPIO.IN,GPIO.PUD_UP)
GPIO.setup(motor1,GPIO.OUT)
GPIO.setup(motor2,GPIO.OUT)
while 1:
    if GPIO.input(switch1)==0:
        GPIO.output(motor1,GPIO.HIGH)
        GPIO.output(motor2,GPIO.LOW)
        print("Clockwise")
        time.sleep(2)
        GPIO.input(switch2)==0
        GPIO.output(motor1,GPIO.LOW)
        GPIO.output(motor2,GPIO.HIGH)
        print("Anti-Clock wise")
        time.sleep(2)

GPIO.output(motor1,GPIO.LOW)
GPIO.output(motor2,GPIO.LOW)
print("stop")

            

