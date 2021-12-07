import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO_TRIGGER = 17
GPIO_ECHO = 27
print("Ultrasonic Distance Measurement")
GPIO.setup(GPIO_TRIGGER,GPIO.OUT) #초음파로 내보낼 트리거 핀 = 출력모드 
GPIO.setup(GPIO_ECHO,GPIO.IN) #반사판을 수신할 에코핀 = 입력모드 

try:
	while True:
		stop = 0
		start = 0
		GPIO.output(GPIO_TRIGGER,False)
		time.sleep(0.2)
		GPIO.output(GPIO_TRIGGER,True)
		time.sleep(0.00001)
		GPIO.output(GPIO_TRIGGER,False)
		#에코핀이 on일 시점을 시작으로 
		while GPIO.input(GPIO_ECHO)==0:
			start=time.time()
		#에코핀이 다시 off되는 시점을 반사파 수신시간
		while GPIO.input(GPIO_ECHO)==1:
			stop=time.time()
		#계산
		elapsed=stop-start

		#초음파는 반사파이기 때문에 실제 이동거리는 2배이므로 2로 다시 나눔
		if(stop and start):
			distance = (elapsed*34000.0)/2
			print("Distance :%.1f cm" % distance)
except KeyboardInterrupt:
	print("Ultrasonic Distance Measurement End")
	GPIO.cleanup()
	
GPIO.cleanup()
