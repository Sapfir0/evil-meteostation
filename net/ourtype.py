import helpers.others as others
import config as cfg
from sensors.gradusnik import Gradusnik


class Ourtype(object):
    weatherDescription = None
    weatherLocation = None
    country = None
    temperature = None
    temperatureInHome = None
    humidity = None
    humidityInHome = None
    pressure = None
    weatherID = None
    windSpeed = None
    icon = None
    windDeg = None
    uvindex = None
    sunsetTime = None
    sunriseTime = None

    def __init__(self, parse=None):
        grad = Gradusnik()
        self.parseOpenweathermapJSON(parse)
        self.temperatureInHome = grad.getTemperature()
        self.humidityInHome = grad.getHumidity()

    def __repr__(self):
        return "temperatureInHome {}, icon {}".format(self.temperatureInHome, self.icon)

    def parseOpenweathermapJSON(self, root):
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

    def setYourJson(self):
        data = {
            "temperatureInHome": self.temperatureInHome,
            "humidityInHome": self.humidityInHome,
            "temperature": self.temperature,
            "humidity": self.humidity,
            "pressure": others.toMmRtSt(self.pressure),
            "sansity": 0,
            "weatherId": self.weatherID,
            "windSpeed": self.windSpeed,
            "windDeg": self.windDeg,
            "icon": self.icon,
            "engWeatherDescription": self.weatherDescription,
            "meteostationId": cfg.meteostationId,
            "sunriseTime": self.sunriseTime,
            "sunsetTime": self.sunsetTime
        }
        return data


def toDict(instance) -> dict:
    data = {
        "temperatureInHome": instance.temperatureInHome,
        "humidityInHome": instance.humidityInHome,
        "temperature": instance.temperature,
        "humidity": instance.humidity,
        "pressure": others.toMmRtSt(instance.pressure),
        "sansity": 0,
        "weatherId": instance.weatherID,
        "windSpeed": instance.windSpeed,
        "windDeg": instance.windDeg,
        "icon": instance.icon,
        "engWeatherDescription": instance.weatherDescription,
        "meteostationId": cfg.meteostationId,
        "sunriseTime": instance.sunriseTime,
        "sunsetTime": instance.sunsetTime
    }
    return data


def toStr(instance) -> str:
    data = "temperatureInHome=" + str(instance.temperatureInHome) \
           + "&humidityInHome=" + str(instance.humidityInHome) \
           + "&temperature=" + str(instance.temperature) \
           + "&humidity=" + str(instance.humidity) \
           + "&pressure=" + str(others.toMmRtSt(instance.pressure)) \
           + "&sansity=" + str(0) \
           + "&weatherId=" + str(instance.weatherID) \
           + "&windSpeed=" + str(instance.windSpeed) \
           + "&windDeg=" + str(instance.windDeg) \
           + "&icon=" + str(instance.icon) \
           + "&engWeatherDescription=" + str(instance.weatherDescription) \
           + "&meteostationId=" + str(cfg.meteostationId) \
           + "&sunriseTime=" + str(instance.sunriseTime) \
           + "&sunsetTime=" + str(instance.sunsetTime)
    return data
