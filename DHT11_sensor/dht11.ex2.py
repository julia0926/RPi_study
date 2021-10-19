import adafruit_dht 
import time
from board import *

PIN = D4 #GPIO 4
dht11 = adafruit_dht.DHT11(PIN, use_pulseio=False)
while True:
    try:
        temperature = dht11.temperature
        humidity = dht11.humidity
        print("Humidity = {:.1f} %".format(humidity), end=' ') 
        print(f"Temperature = {temperature: .1f} *C")
    except Exception as e: 
        print(e)
    time.sleep(2.0)