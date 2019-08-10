import dht
import config as cfg
from machine import Pin

class Gradusnik():
    temperature = 0
    humidity = 0
    illumination = 0

    pin = cfg.defineAnalog(cfg.DHTPIN)
    grad = dht.DHT11(Pin(pin))

    def start(self):
        self.grad.measure()


    def getTemperature(self):
        temperature = self.grad.temperature()
        return temperature
    
    def getHumidity(self):
        humidity = self.grad.humidity()
        return humidity





