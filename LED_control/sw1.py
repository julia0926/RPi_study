import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

GPIO.setup(12,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(16,GPIO.OUT)

i=0
while True:
    if(GPIO.input(12)==1):
        if i==0: i=1
        else: i=0
    GPIO.output(16,i)
    
GPIO.cleanup()
