import smbus
import time

#Get I2C bus
bus = smbus.SMBus(1)
#IC address
ADDR = 0x69

bus.write_byte_data(ADDR, 0x20, 0x0F) #X,Y,Z enabled
bus.write_byte_data(ADDR, 0x23, 0x30) #update

try:
    while 1:
        time.sleep(0.1)

        #Read X-Axis LSB first
        data0 = bus.read_byte_data(ADDR, 0x28)
        data1 = bus.read_byte_data(ADDR, 0x29)
        xGyro = data1 * 256 + data0
        if xGyro > 32767:
            xGyro -= 65536 
        #Read Y-Axis LSB first
        data0 = bus.read_byte_data(ADDR, 0x2A)
        data1 = bus.read_byte_data(ADDR, 0x2B)
        yGyro = data1 * 256 + data0
        if yGyro > 32767:
            yGyro -= 65536 

        #Read Z-Axis LSB first
        data0 = bus.read_byte_data(ADDR, 0x2C)
        data1 = bus.read_byte_data(ADDR, 0x2C)
        zGyro = data1 * 256 + data0
        if zGyro > 32767:
            zGyro -= 65536 
        
        print("Rotation in X,Y,Z: {},{},{}".format(xGyro,yGyro,zGyro))
        
except Exception as e: print(e)