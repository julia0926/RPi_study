import picamera
import RPi.GPIO as IoPort
import time

def KeyHit(channel):
	global KeyVal
	if channel == Key1:
		KeyVal = 1
	elif channel == Key1:
		KeyVal = 2

def VideoRecord():
	global KeyVal, VrlNo
	print("recoding....")
	str1 = 'Video' + str(VrlNo) + 'h.264'
	camera.start_recoding(str1)
	while True:
		if KeyVal == 1: #22핀 스위치 누르면
			break
	KeyVal = 0
	camera.stop_recoding()
	print(str1, 'is Created')
	VrlNo = VrlNo + 1 

def Capture():
	global SrlNo
	str1 = 'cam_' + strNo + '.jpg'
	camera.capture(str1)
	print(str1, 'is Created')
	SrlNo = SrlNo + 1

Key1 = 22
Key2 = 27
IoPort.setmode(IoPort.BCM)
IoPort.setup(Key1, IoPort.IN)
IoPort.setup(Key2, IoPort.IN)
# 인터럽트가 트리거 되면 호출되는 콜백을 등록하는 함수
IoPort.add_event_detect(Key1,IoPort.FALLING,callback=KeyHit) 
IoPort.add_event_detect(Key2,IoPort.FALLING,callback=KeyHit) 
KeyVal = 0
SrlNo = 0
VrlNo = 0
camera = picamera.PiCamera()
camera.start_preview()
camera.preview.fullscreen = False
camera.preview.window = (0, 0, 640, 480)
	