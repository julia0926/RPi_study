import RPi.GPIO as GPIO
import time

GPIOIN = 17
GPIOOUT = 27

GPIO.setmode(GPIO.BCM)
print("detection start")

GPIO.setup(GPIOIN, GPIO.IN) #센서
GPIO.setup(GPIOOUT, GPIO.OUT) #출력 LED

try:
    while True: # 센서 출력 값을 읽음
        state = GPIO.input(GPIOIN)
        if(state == True):
            print("모션 감지")
        else:
            print("모션 감지 실패")
        GPIO.output(GPIOOUT, state) #센서 검출 값을 LED로
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
print("END!!!")