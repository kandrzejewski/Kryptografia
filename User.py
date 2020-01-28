from Crypto.PublicKey import RSA
from Crypto.Util import randpool

import Vigenere

import HC_SR04
import BH1750
import BME280
import DHT_11
import HMC5883L

def get_values_from_sensors(_sensor_values):
    distance = HC_SR04.distance()
    illuminance = BH1750.readLight()
    temperature, pressure, humidity = BME280.read_temp_press_hum()
    humidity2, temperature2 = DHT_11.temperature_humidity()
    heading_angle, x, y, z = HMC5883L.read_magnetometer()

    _sensor_values.append(distance)
    _sensor_values.append(illuminance)
    _sensor_values.append(temperature)
    _sensor_values.append(pressure)
    _sensor_values.append(humidity)
    _sensor_values.append(temperature2)
    _sensor_values.append(humidity2)
    _sensor_values.append(x)
    _sensor_values.append(y)
    _sensor_values.append(z)

    print("________________Values from sensors _________________")
    if distance is not None:
        print('Distance={0:0.4f}cm'.format(distance))
    else:
        print('Failed to get reading from HC-SR04. Try again!')
        return False

    if illuminance is not None:
        print("Illuminance=" + format(illuminance, '.4f') + " lx")
    else:
        print('Failed to get reading from BH1750. Try again!')
        return False

    if temperature is not None and pressure is not None and humidity is not None:
        print "Temperature= ", temperature, "C"
        print "Pressure= ", pressure, "hPa"
        print "Humidity= ", humidity, "%"
    else:
        print('Failed to get reading from BME280!')
        return False

    if humidity2 is not None and temperature2 is not None:
        print('Temperature={0:0.4f}*C\nHumidity={1:0.4f}%'.format(temperature2, humidity2))
    else:
        print('Failed to get reading from DHT11. Try again!')

    if x is not None and y is not None and z is not None:
        print('x= %d \ny= %d \nz= %d' % (x, y, z))
    else:
        print('Failed to get reading from HMC5883L!')

    print("______________________________________________________")
    return True


class  User:
    vigenere_key = ""

    def __init__(self):
        pass

    def start_transmission(self):
        return True

    def get_public_key(self):
        blah = randpool.RandomPool()
        self.rsa_key = RSA.generate(1024, blah.get_bytes)
        rsa_public_key = self.rsa_key.publickey()
        return rsa_public_key

    def generate_vigenere_key(self):
        sensor_values = []
        if get_values_from_sensors(sensor_values):
            vigenere_key_int = long(sensor_values[0] * sensor_values[1] * sensor_values[2]
                                   * sensor_values[3] * (sensor_values[4]
                                   * pow(sensor_values[0], sensor_values[2]))
                                   + (sensor_values[5]
                                   * pow(sensor_values[6], sensor_values[7])
                                   * sensor_values[8])
                                   * sensor_values[9])
            i = 0
            str_priv_key = str(vigenere_key_int)
            while i < len(str_priv_key) - 1:
                self.vigenere_key += chr(int(str_priv_key[i:i + 1]) % 26 + 65)
                i += 2
            return self.vigenere_key
        else:
            return False

    def encrypt_rsa(self, _vigenere_key, _rsa_public_key):
        return _rsa_public_key.encrypt(_vigenere_key,32)

    def decrypt_rsa(self, _encrypted_vigenere_key):
        self.decrypted_vigenere_key = self.rsa_key.decrypt(_encrypted_vigenere_key)
        return True

    def encrypt_text_vigenere(self):
        message = raw_input("Enter a message: ")
        return Vigenere.encrypt(message, self.vigenere_key);

    def decrypt_text_vigenere(self, _encrypted_text_vigenere):
        return Vigenere.decrypt(_encrypted_text_vigenere, self.decrypted_vigenere_key)