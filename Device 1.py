import HC_SR04
import Vigenere
import BH1750
import BME280
from Crypto.Hash import MD5
from Crypto.PublicKey import RSA
from Crypto.Util import randpool
import re


def get_values_from_sensors():
    get_values_from_sensors.distance = HC_SR04.distance()
    get_values_from_sensors.illuminance = BH1750.readLight()
    get_values_from_sensors.temperature, get_values_from_sensors.pressure, \
        get_values_from_sensors.humidity = BME280.read_temp_press_hum()

    if get_values_from_sensors.distance is not None:
        print('Distance={0:0.4f}cm'.format(get_values_from_sensors.distance))
    else:
        print('Failed to get reading from HC-SR04. Try again!')
        return False

    if get_values_from_sensors.illuminance is not None:
        print("Illuminance=" + format(get_values_from_sensors.illuminance, '.4f') + " lx")
    else:
        print('Failed to get reading from BH1750. Try again!')
        return False

    if get_values_from_sensors.temperature is not None and get_values_from_sensors.pressure \
            is not None and get_values_from_sensors.humidity is not None:
        print "Temperature= ", get_values_from_sensors.temperature, "C"
        print "Pressure= ", get_values_from_sensors.pressure, "hPa"
        print "Humidity= ", get_values_from_sensors.humidity, "%"
    else:
        print('Failed to get reading from BME280!')
        return False
    return True

def get_public_key():
    blah = randpool.RandomPool()
    get_public_key.RSAKey = RSA.generate(1024, blah.get_bytes)
    RSAPubKey = get_public_key.RSAKey.publickey()
    return RSAPubKey

def send_message():
    if get_values_from_sensors():
        priv_key1 = int(get_values_from_sensors.distance * get_values_from_sensors.illuminance
                        * get_values_from_sensors.temperature * get_values_from_sensors.pressure
                        * (get_values_from_sensors.humidity
                        * pow(get_values_from_sensors.distance,get_values_from_sensors.temperature)))
        print("Priv key 1: " + str(priv_key1))
        i = 0
        vigenere_key = ""
        str_priv_key = str(priv_key1)
        while i < len(str_priv_key) - 1:
            vigenere_key += chr(int(str_priv_key[i:i+1]) % 23 +65)
            i += 2
        print("Vigenere key: " + vigenere_key)
        print("len: " +  str(len(str_priv_key) - 1))
        ReciverPubKey = get_public_key();
        encoded_vigenere_key = ReciverPubKey.encrypt(vigenere_key,32)
        message = raw_input("Enter a message:")
        encoded_message = Vigenere.encrypt(message, vigenere_key);

        encrypted_vigenere_key = encoded_vigenere_key
        decrypted_vigenere_key = get_public_key.RSAKey.decrypt(encrypted_vigenere_key)
        print("decrypt: " + decrypted_vigenere_key)
        decoded_message = Vigenere.decrypt(encoded_message,decrypted_vigenere_key)
        print("decrypted message: " + decoded_message)


#def receive_message():


send_message()

