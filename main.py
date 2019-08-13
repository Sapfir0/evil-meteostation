import config as cfg
from net.wifi import WIFI
import uasyncio as asyncio


queryToServerTime = 10*60  # в секундах все
displayOnLCDTime = 6

net = WIFI()

async def sleeper(duration):
    await asyncio.sleep(duration)


def queryToServer():
    print("In query")
    weatherData = net.getQuery(cfg.openweathermapUrl)
    net.postQuery(weatherData)

queryToServer()
ioloop = asyncio.get_event_loop()
ioloop.call_later(queryToServerTime, queryToServer)
ioloop.run_forever()
