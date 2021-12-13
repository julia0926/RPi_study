from flask import Flask
import Rpi.GPIO as GPIO

app = Flask(__name__)

LED = 8
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED, GPIO.OUT, inital=GPIO.LOW)

@app.route('/')
def index():
    return 'This is main page'

@app.route('/led/on')
def led_on():
	GPIO.output(LED, GPIO.HIGH)
	return "LED ON"

@app.route('/led/off')
def led_off():
	GPIO.output(LED, GPIO.LOW)
	return "LED OFF"

@app.route('/gpio/cleanup')
def gpio_cleanup():
	GPIO.cleanup()
	return "GPIO CLEANUP"


#app.run() 이 호출되면 웹 서버 동작
if __name__ == '__main__':
    app.run(host='0.0.0.0')  # 어떤 IP 요청도 수락
