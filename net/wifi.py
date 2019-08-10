import config as cfg
import helpers.others as others

class WIFI(object):
    weatherDescription = None
    weatherLocation = None
    country = None
    temperature = None
    humidity = None
    pressure = None
    weatherID = None
    windSpeed = None
    icon = None
    windDeg = None
    uvindex = None
    sunsetTime = None
    sunriseTime = None

    def __init__(self):
        import upip
        upip.install("urequests")

    def getQuery(self, url):
        import urequests
        r = urequests.get(url)
        self.parseWeatherJSON(r.json())
        r.close()

    def parseWeatherJSON(self, root):
        self.weatherLocation = root["name"]
        self.country = root["sys"]["country"]
        self.temperature = root["main"]["temp"]
        self.humidity = root["main"]["humidity"]
        self.pressure = root["main"]["pressure"]
        self.windSpeed = root["wind"]["speed"]
        self.windDeg = root["wind"]["deg"]
        self.sunriseTime = root["sys"]["sunrise"]
        self.sunsetTime = root["sys"]["sunset"]
        try:
            self.weatherDescription = root["weather"]["description"]
            self.weatherID = root["weather"]["id"]
            self.icon = root["weather"]["icon"]
        except:
            self.weatherDescription = root["weather"][0]["description"]
            self.weatherID = root["weather"][0]["id"]
            self.icon = root["weather"][0]["icon"]


    
    def postQuery(self, data):
        from gradusnik import Gradusnik
        import urequests

        grad = Gradusnik()

        data = {
            "temperatureInHome": grad.getTemperature(),
            "humidityInHome": grad.getHumidity(),
            "temperature": self.temperature,
            "humidity": self.humidity,
            "pressure": others.toMmRtSt(self.pressure),
            "sansity": 0 ,
            "weatherId": self.weatherID,
            "windSpeed": self.windSpeed,
            "windDeg": self.windDeg,
            "icon": self.icon,
            "engWeatherDescription": self.weatherDescription,
            "meteostationId": cfg.meteostationId,
            "sunriseTime": self.sunriseTime,
            "sunsetTime": self.sunsetTime
        }
        #print(data)
        headers = {'content-type': 'application/json'}

        #r = urequests.post("http://api.openweathermap.org/data/2.5/weather?id={}&units=metric&APPID={}".format(cfg.cityId, cfg.APIKEY), data=data, headers=headers)

        #r.close()