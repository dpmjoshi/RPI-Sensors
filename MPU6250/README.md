/* Written By: Dnyanesh P. Joshi

/* Date: 03/09/2015

/* Description: MPU6250 driver for Raspberry Pi B+ 

/* I2C bus 1 used on RPI 
 

   Procedure to test this file on RPI B+
   
   Step 1) uncomment the I2C from blacklist 
	   
	   // Type
 	   Sudo nano /etc/modprobe.d/raspi-blacklist.conf
	   // now comment out the i2c blacklsit command by adding
	   // # infront of it, your 'raspi-blacklist.conf' should look like 
	   blacklist spi-bmc2708	
	   blacklist i2c-bmc2708

   Step 2) Add I2C module 
 	
 	   // Type
 	   sudo nano /etc/modules
 	   // and add following line into the file 
 	   i2c-dev
 	   // save the file 
 	   
   Step 3) Install Python-smbus and i2c-tools 
   
   	   // Type	
    	   sudo apt-get python-smbus i2c-tools 
    
   Step 4) Now shutdown RPI and connect MPU9250 sensor to it 
   
    	   // Type 	 	   
 	   i2cdetect -y 1
 	   // This will show a slave address in hex map 
 	   // If you dont see anything then check your sensor connections.
    
   Step 5) execute MPU6250.py 
   
   	   // Type 
   	   python MPU6250.py
    	   // you should see sensor output on the screen 	
    	   


Creating Apache web server on RPI 
https://www.raspberrypi.org/documentation/remote-access/web-server/apache.md



















