# coding=utf-8
import RPi.GPIO as GPIO
from time import sleep
from gpiozero import MotionSensor

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(4, GPIO.IN)
GPIO.setwarnings(False)

pir = MotionSensor(4)

def motion_sensor_event():
    if pir.when_motion:
        print "Czujnik aktywny"
        GPIO.output(21, GPIO.HIGH)
    else:
        print "Czujnik nieaktywny."
        GPIO.output(21, GPIO.LOW)

def test():
    old_pir = 2
    try:
        while True:

            if pir.when_motion != old_pir:
                old_pir = pir.when_motion
                motion_sensor_event()
            else:
                sleep(1)
    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    test()