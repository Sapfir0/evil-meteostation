def getWeatherData(self):
    #http req;
    requestStr = "id=" + cityId +"&units=metric&APPID=" + APIKEY;
    req.getQuery("api.openweathermap.org", "/data/2.5/weather", requestStr);
    result = req.getResponseFromServer(result);
    parseWeatherJSON(result);
    
    getUVindexData();
}

def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('<essid>', '<password>')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())
