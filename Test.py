import RPi.GPIO as GPIO
import HC_SR04
import DHT_11
import Vigenere
import BH1750
import HMC5883L

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
illuminance = BH1750.readLight()
heading_angle, x, y, z = HMC5883L.read_magnetometer()


if humidity is not None and temperature is not None:
    print('Tempherature={0:0.4f}*C\nHumidity={1:0.4f}%'.format(temperature, humidity))
else:
    print('Failed to get reading from DHT11. Try again!')

if distance is not None:
    print('Distance={0:0.4f}cm'.format(distance))
else:
    print('Failed to get reading from HC-SR04. Try again!')

if illuminance is not None:
    print("Illuminance=" + format(illuminance, '.4f') + " lx")
else:
    print('Failed to get reading from BH1750. Try again!')

if heading_angle is not None:
    print('x= %d \ny= %d \nz= %d' %(x, y, z))
    print("Heading angle= %d angle" %heading_angle)
else:
    print('Failed to get reading from BH1750. HMC5883L!')

ciphertext = Vigenere.encrypt('KOCHAMFPGA', 'MELOSIK')
plaintext = Vigenere.decrypt(ciphertext, 'MELOSIK')
print('Wartosc zaszyfrowana: ' + ciphertext)
print('Wartosc odszyfrowana: ' + plaintext)
