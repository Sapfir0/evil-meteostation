import dht
import cfg
import machine

class Gradusnik():
    temperature = 0
    humidity = 0
    illumination = 0

    grad = dht.DHT11(Pin(cfg.DHTPIN))

    def start(self):
        self.grad.measure()


    def getTemperature(self):
        temperature = self.grad.temperature()
        return temperature
    
    def getHumidity(self):
        humidity = self.grad.humidity()
        return humidity




