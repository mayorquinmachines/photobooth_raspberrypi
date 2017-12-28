import RPi.GPIO as GPIO
import subprocess
import time
from datetime import datetime

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(17)
    if input_state == False:
        tm_stmp = datetime.now().strftime("%Y_%m_%d_%H_%M")
        time.sleep(5)
        subprocess.call('raspistill -o /home/pi/photos/{}.jpg -rot 90'.format(tm_stmp), shell=True)
        time.sleep(0.2)
