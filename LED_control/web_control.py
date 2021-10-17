import RPi.GPIO as GPIO
from flask import Flask, render_template

state = 'off'
app = Flask(__name__)

def led_on_off(onoff): #LED 점멸 코드 
    if onoff == 'on':
        GPIO.output(21,0) #LED 켜져있으면 끔
    else:
        GPIO.output(21,1) #꺼져 있으면 킴

@app.route('/')
def index():
    return render_template('index.html', state=state)
@app.rount('/led/<onoff>') # /led/ 링크를 호출하면 onoff 인자가 들어가 바뀜
def led(onoff):
    global state
    led_on_off(state)
    print('led %s'%state)
    return render_template('index.html', state=onoff) #다시 렌더링되서 상태 바뀜

GPIO.setmode(GPIO.BCM) #GPIO 핀 번호 사용
GPIO.setup(21,GPIO.OUT) #21번을 출력 모드로
#led_on_off('off')

if __name__ == '__main__':
    app.run(host='0.0.0.0') #서버 시작 
    GPIO.cleanup() #종료
