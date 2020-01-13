import RPi.GPIO as GPIO
import HC_SR04
import DHT_11
import Vigenere


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
humidity, temperature = DHT_11.temperature_humidity(GPIO_DHT)

if humidity is not None and temperature is not None:
    print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
else:
    print('Failed to get reading from DHT11. Try again!')

if distance is not None:
    print('Dist={0:0.1f}cm'.format(distance))
else:
    print('Failed to get reading from HC-SR04. Try again!')

ciphertext = Vigenere.encrypt('KOCHAMFPGA', 'MELOSIK')
plaintext = Vigenere.decrypt(ciphertext, 'MELOSIK')
print('Wartosc zaszyfrowana: ' + ciphertext)
print('Wartosc odszyfrowana: ' + plaintext)
