import dht
import config as cfg
from machine import Pin


class Gradusnik():
    temperature = 0
    humidity = 0
    illumination = 0

    pin = cfg.defineAnalog(cfg.DHTPIN)
    grad = dht.DHT11(Pin(2))

    def __init__(self):
        self.grad.measure()
        self.getTemperature()
        self.getHumidity()

    def getTemperature(self):
        temperature = self.grad.temperature()
        return temperature
    
    def getHumidity(self):
        humidity = self.grad.humidity()
        return humidity

    def getParams(self):
        return self.temperature, self.humidity




