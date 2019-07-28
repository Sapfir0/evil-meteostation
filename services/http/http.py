import upip
upip.install("urequests")

import urequests


def getQuery(url):
    r = urequests.get("http://api.openweathermap.org/data/2.5/weather?id=472757&units=metric&APPID=9881fdc10d1d14339a3a6514d415efa4")
    print(r.json())
    r.close()


def postQuery(url, requestStr):
    