# tkinter 이용해서 LED 켜고 끄는 GUI 프로그램 

import RPi.GPIO as GPIO
from tkinter import *
GPIO.setmode(GPIO.BOARD)
LED=16
GPIO.setup(LED,GPIO.OUT,initial=GPIO.LOW) #초기 값을 0으로 16번 핀을 출력으로 
def func(): #켰다 껐따 하는 함수
    GPIO.output(LED, not GPIO.input(LED)) 

root = Tk()
label = Label(root,text='Press Button')
label.pack()
button = Button(root, text='LED', command=func)
button.pack() #버튼을 배치
root.mainloop() #root 표시

GPIO.cleanup()