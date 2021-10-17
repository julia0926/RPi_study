import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
count = 0
def handler(channel):
    global count
    count += 1
    print(count)

GPIO.setup(12,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(12, GPIO.RISING, callback=handler)
while True:
    time.sleep(1)
