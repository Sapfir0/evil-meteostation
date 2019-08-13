# import config as cfg
# from net.wifi import WIFI
import uasyncio as asyncio
#
#
# queryToServerTime = 10#*60  # в секундах все
# displayOnLCDTime = 6
#
#
# async def sleeper(duration):
#     await asyncio.sleep(duration)
#
#
# async def queryToServer():
#     print("In query")
#
#     weatherData = net.getQuery(cfg.openweathermapUrl)
#     net.postQuery(weatherData)
#
# queryToServer()
# print("Before loop")
# net = WIFI()
# ioloop = asyncio.get_event_loop()
# print("In loop")
#
# ioloop.call_later(queryToServerTime, queryToServer)
# ioloop.run_forever()


def event_loop():
    led_1_time = 0
    led_2_time = 0
    switch_state = switch.state()  # Current state of a switch
    while True:
        time_now = utime.time()
        if time_now >= led_1_time:  # Flash LED #1
            led1.toggle()
            led_1_time = time_now + led_1_period
        if time_now >= led_2_time:  # Flash LED #2
            led2.toggle()
            led_2_time = time_now + led_2_period
        # Handle LEDs 3 upwards

        if switch.value() != switch_state:
            switch_state = switch.value()
            # do something
