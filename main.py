#import esp
import config as cfg
from net.wifi import WIFI
net = WIFI()


requestStr = "http://api.openweathermap.org/data/2.5/weather?id={}&units=metric&APPID={}".format(cfg.cityId, cfg.APIKEY)
weatherData = net.getQuery(requestStr)
#net.postQuery()




