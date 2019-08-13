import config as cfg
from net.ourtype import Ourtype
import urequests


class WIFI(object):
    def getQuery(self, url: str) -> dict:
        r = urequests.get(url)
        data = Ourtype(r.json())
        r.close()
        return data
    
    def postQuery(self, data):
        from net.ourtype import toDict, toStr
        requestJson = toDict(data)

        link = "https://meteo-server.herokuapp.com/meteostationData"
        r = urequests.post(link, json=requestJson) # если json= , то передаем в бади, если data= , то в урле

        print(r.text)  # Успешно
        r.close()
