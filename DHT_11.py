import Adafruit_DHT
import RPi.GPIO as GPIO

sensor = Adafruit_DHT.DHT11
# GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
GPIO_DHT = 17

def temperature_humidity():
    return Adafruit_DHT.read_retry(sensor, GPIO_DHT)