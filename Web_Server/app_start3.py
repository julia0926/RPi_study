from flask import Flask, request
import RPi.GPIO as GPIO

app = Flask(__name__)

LED = 8
GPIO.setMode(GPIO.BOARD) #물리핀 사용 
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)

@app.route("/")
def helloworld():
	return "Hello world"

#쿼리 스트링이니까 뒤에 매개변수 필요 업슴
@app.route("/led")
def led():
	state = request.args.get("state", "error")
	if state == "on":
		GPIO.output(LED, GPIO.HIGH)
	elif state == "off":
		GPIO.output(LED, GPIO.LOW)
    elif state == "error":
        return "Missing Query String State"
    else:
        return "Wrong Query String State "
	return "LED" + state

@app.route("/gpio/cleanup")
def gpio_cleanup():
	GPIO.cleanup()
	return "GPIO CLEANUP"

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000)