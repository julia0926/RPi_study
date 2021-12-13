from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'This is main page'

@app.route('/sub')
def sub():
    return 'This is sub page'

@app.route('/led/<state>')
def led(state):
    if state=='on' or state=='off':
        str = 'LED in now %s' %state
    else:
        str = 'Invalid Pages'
    return str

#app.run() 이 호출되면 웹 서버 동작
if __name__ == '__main__':
    print('Webserver starts')
    app.run(host='0.0.0.0')  # 어떤 IP 요청도 수락 