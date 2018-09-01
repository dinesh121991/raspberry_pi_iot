import Adafruit_DHT
import RPi.GPIO as GPIO
import time
# Set sensor type : Options are DHT11,DHT22 or AM2302
sensor=Adafruit_DHT.DHT11
 
# Set GPIO sensor is connected to
#gpio=17

#led = 22
#set numbering mode for the program

## Set GPIO sensor is connected to
GPIO.setmode(GPIO.BOARD)
gpio=11

led = 15

#setup led(pin 8) as output pin
#GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT,initial=0)
 
 
# Use read_retry method. This will retry up to 15 times to
 
# Reading the DHT11 is very sensitive to timings and occasionally
# the Pi might fail to get a valid reading. So check if readings are valid.
while True:
    # get a sensor reading (waiting 2 seconds between each retry).
    humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)

    if humidity is not None and temperature is not None and humidity > 20:
        print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
            #turn on, set as HIGH or 1
        GPIO.output(led,GPIO.HIGH)
        print("ON")
        time.sleep(1)
        #turn off, set as LOW or 0
        GPIO.output(led, GPIO.LOW)
        print("OFF")
        time.sleep(1)
    else:
        print('Failed to get reading. Try again!')
        print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))



