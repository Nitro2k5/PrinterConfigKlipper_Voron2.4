import RPi.GPIO as GPIO
import subprocess
from time import sleep
from signal import pause

#define where you connected the button switch
buttonpin = 26

#time interval to check button state after you press (and hold) the button
timestep = 0.1


def init_gpio():
    # supress warnings and use GPIO pin numbering
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    # set buttonpin as input
    GPIO.setup(buttonpin, GPIO.IN, pull_up_down = GPIO.PUD_UP)


def reboot():
    #adds custom text to console output after KlipperScreen is terminated
    #if you add your own custom ascii art \ needs to be escaped with \\
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print('                                 ____  _____ ____   ___   ___ _____         ')
    print('                                |  _ \| ____| __ ) / _ \ / _ \_   _|        ')
    print('                         _____  | |_) |  _| |  _ \| | | | | | || |    _____ ')
    print('                        |_____| |  _ <| |___| |_) | |_| | |_| || |   |_____|')
    print('                          __    |_|_\_\_____|____/ \___/_\___/_|_| _  _     ')
    print('                          \ \   / / _ \|  _ \ / _ \| \ | | |___ \ | || |    ')
    print('                           \ \ / / | | | |_) | | | |  \| |   __) || || |_   ')
    print('                            \ V /| |_| |  _ <| |_| | |\  |  / __/ |__   _|  ')
    print('                             \_/  \___/|_| \_\\\\___/|_| \_| |_____(_) |_|  ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    
    #reboot rpi
    subprocess.call(["shutdown", "-r", "now"])


def shutdown():
    #adds custom text to console output after KlipperScreen is terminated
    #if you add your own custom ascii art \ needs to be escaped with \\
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print('                        ____  _   _ _   _ _____ ____   _____        ___   _         ')
    print('                       / ___|| | | | | | |_   _|  _ \ / _ \ \      / / \ | |        ')
    print('                _____  \___ \| |_| | | | | | | | | | | | | \ \ /\ / /|  \| |  _____ ')
    print('               |_____|  ___) |  _  | |_| | | | | |_| | |_| |\ V  V / | |\  | |_____|')
    print('                       |____/|_| |_|\___/__|_| |____/ \___/ _\_/\_/_ |_| \_|        ')
    print('                          \ \   / / _ \|  _ \ / _ \| \ | | |___ \ | || |            ')
    print('                           \ \ / / | | | |_) | | | |  \| |   __) || || |_           ')
    print('                            \ V /| |_| |  _ <| |_| | |\  |  / __/ |__   _|          ')
    print('                             \_/  \___/|_| \_\\\\___/|_| \_| |_____(_) |_|          ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    
    #shut down shelly after 30 sec
    import os
    os.system("wget -q -O /dev/null \"http://192.168.178.141/relay/0?turn=on&timer=30\"")
    
    #shutdown rpi
    subprocess.call(["shutdown", "-h", "now"])


def check_periodically(channel):
    timecounter = 0
    
    # button pressed and released befor <1sec
    while timecounter < 1:
        if GPIO.input(buttonpin):
            return
        sleep(timestep)
        timecounter = timecounter + timestep
    
    # button pressed and released between >=1sec & <3sec
    while timecounter < 3:
        if GPIO.input(buttonpin):
            reboot()
            return
        sleep(timestep)
        timecounter = timecounter + timestep
    
    # button pressed and holded for >=3sec
    shutdown()


def init_and_listen():
    init_gpio()
    
    # buttonpin as interrupt input
    GPIO.add_event_detect(buttonpin, GPIO.FALLING,
                          callback=check_periodically, bouncetime=200)
    
    try:
        #keep script running
        pause()
    except (SystemExit, KeyboardInterrupt):
        GPIO.cleanup()


if __name__ == "__main__":
    init_and_listen()

