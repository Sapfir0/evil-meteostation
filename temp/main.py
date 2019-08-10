#import esp
import config as cfg
from wifi import WIFI
net = WIFI()

net.do_connect()

requestStr = "http://api.openweathermap.org/data/2.5/weather?id={}&units=metric&APPID={}".format(cfg.cityId, cfg.APIKEY)
weatherData = net.getQuery(requestStr)
net.postQuery()




