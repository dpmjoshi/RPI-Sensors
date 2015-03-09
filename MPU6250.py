#Created By: Dnyanesh P Joshi
#
#
#
#
import smbus
import time
import os
import RPi.GPIO as GPIO


MPU_ADD    = 0x68
ACC_X_DATA = 0x3B
ACC_Y_DATA = 0x3D
ACC_Z_DATA = 0x3F
GYR_X_DATA = 0x43
GYR_Y_DATA = 0x45
GYR_Z_DATA = 0x47

class mpu9250():
    myBus=""
    if GPIO.RPI_REVISION == 1:
	    myBus=0
    elif GPIO.RPI_REVISION == 2:
	    myBus=1   
    elif GPIO.RPI_REVISION == 3:
	    myBus=1  	 

    print "#---------------------------------------------"	
    print "# Raspberry Pi GPIO Revision : " + str(GPIO.RPI_REVISION) 	
    print "#---------------------------------------------"	

    i2c = smbus.SMBus(myBus)
    def init(self):
        print("Initializing MPU9250...")
	self.i2c.write_byte_data(MPU_ADD, 0x6B, 0x01)
	self.i2c.write_byte_data(MPU_ADD, 0x1A, 0x05)
		

    def getValueX(self):
	return self.i2c.read_byte_data(MPU_ADD, ACC_X_DATA)
    
    def getValueY(self):
	return self.i2c.read_byte_data(MPU_ADD, ACC_Y_DATA)
	

def main():	
    print "MPU9250 driver"		
    Acc = mpu9250()
    Acc.init()
    for a in range(100):
	Acc_X = Acc.getValueX()
	Acc_Y = Acc.getValueY()
	print str(Acc_X) + "  " + str(Acc_Y)
    return 
	
main()	

    
    

    


















