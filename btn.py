import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD) #물리 핀 번호로 설정
GPIO.setup(12, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
count = 0

while True:
    value = GPIO.input(12) #12 값을 읽어 High라면
    if value == True:
        count += 1
        print(count)
    time.sleep(0.1)

