import RPi.GPIO as GPIO
import HC_SR04
import DHT_11
import Vigenere
import BH1750
import HMC5883L
import BME280

# GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

# set GPIO Pins
GPIO_TRIGGER = 18
GPIO_ECHO = 24
GPIO_DHT = 17

# set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

distance = HC_SR04.distance(GPIO_TRIGGER, GPIO_ECHO)
illuminance = BH1750.readLight()
temperature,pressure,humidity = BME280.read_temp_press_hum()



def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in xrange(3, int(num ** 0.5) + 2, 2):
        if num % n == 0:
            return False
    return True

def Encrypt():
    print("Im in Encrypt")

def Decrypt():
    print("Im in Decrypt")


if __name__ == '__main__':
    p = int(raw_input("Enter a prime number (17, 19, 23, etc): "))
    q = int(raw_input("Enter another prime number (Not one you entered above): "))
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    priv_key1 = int((distance % 100 + illuminance + temperature * pressure) * humidity)
    print("Priv key 1: " + str(priv_key1))
    key1 = pow(p, priv_key1) % q
    print("Key1: " + str(key1))