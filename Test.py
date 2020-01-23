import HC_SR04
import DHT_11
import Vigenere
import BH1750
import HMC5883L
import BME280

distance = HC_SR04.distance()
humidity, temperature = DHT_11.temperature_humidity()
illuminance = BH1750.readLight()
heading_angle, x, y, z = HMC5883L.read_magnetometer()
temperature2,pressure,humidity2 = BME280.read_temp_press_hum()

if humidity is not None and temperature is not None:
    print('Temperature={0:0.4f}*C\nHumidity={1:0.4f}%'.format(temperature, humidity))
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
    print('Failed to get reading from HMC5883L!')

if temperature2 is not None and pressure is not None and humidity2 is not None:
    print "Temperature2= ", temperature2, "C"
    print "Pressure= ", pressure, "hPa"
    print "Humidity2= ", humidity2, "%"
else:
    print('Failed to get reading from BME280!')


ciphertext = Vigenere.encrypt('KOCHAMFPGA', 'MELOSIK')
plaintext = Vigenere.decrypt(ciphertext, 'MELOSIK')
print('Wartosc zaszyfrowana: ' + ciphertext)
print('Wartosc odszyfrowana: ' + plaintext)
