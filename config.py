cityId = "472757"
APIKEY = "9881fdc10d1d14339a3a6514d415efa4"
ssid = "WiFi-DOM.ru-1520"
password = "sapfir1997"

# pins
DHTPIN = "D4"
photoresistor = "A0"
LedLight = "D6"
rgbPins = ["D5", "D8", "D7"]

ourServer = "meteo-server.herokuapp.com"
meteostationId = 1


def defineAnalog(nodemcuPin):
    physicalPins = ["D0", "D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9", "D10", "D11", "D12"]
    programmPins = [16, 5, 4, 0, 2, 14, 12, 13, 15, 3, 1, 9, 10]
    if (len(physicalPins) != len(programmPins)):
        raise Exception("Oh no")
    
    for i, pin in enumerate(physicalPins):
        if nodemcuPin == pin:
            return programmPins[i]