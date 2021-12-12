import Rpi.GPIO as GPIO
import time

pwm_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(pwm_pin, GPIO.OUT) #18번 핀을 출력으로
Pwm = GPIO.PWM(pwm_pin, 50) #50Hz의 PWM 
duty = 3.0
Pwm.start(duty)
time.sleep(0,1)

try:
    while True:
        cmd = input("Command: f/r:")
        direction = cmd[0]
        if direction == "f": #정회전
            duty += 0.5
        else: #역회전
            duty -= 0.5
        if duty < 3.0: #duty 최소 
            duty = 3.0
        elif duty > 12: #duty 최대
            duty = 12
        print("angle =", (duty-3.0)*20)
        Pwm.changeDutyCycle(duty) # duty 싸이클 변경

finally:
    Pwm.stop()
    GPIO.cleanup()