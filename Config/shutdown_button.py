import time
import RPi.GPIO as GPIO

shutdown_pin = 26

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(shutdown_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def shut_down():
    import os
    os.system("wget -q -O /dev/null \"http://192.168.178.141/relay/0?turn=on&timer=30\"")
    os.system("shutdown now -h")

while True:
    time.sleep(1.0)
    if GPIO.input(shutdown_pin) == False:
        counter = 0
        while GPIO.input(shutdown_pin) == False:
            counter += 1
            time.sleep(0.25)
            if counter > 11:
                shut_down()
