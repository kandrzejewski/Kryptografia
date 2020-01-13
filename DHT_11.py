import Adafruit_DHT

sensor = Adafruit_DHT.DHT11

def temperature_humidity(GPIO_DHT):
    return Adafruit_DHT.read_retry(sensor, GPIO_DHT)