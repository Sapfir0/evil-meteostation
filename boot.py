import config as cfg


def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        sta_if.active(True)
        sta_if.connect(cfg.ssid, cfg.password)
        while not sta_if.isconnected():
            pass
    print('net config:', sta_if.ifconfig())


def install_modules():
    import upip
    import uasyncio
    upip.install("urequests")
    upip.install('micropython-uasyncio')
    upip.install('micropython-uasyncio.synchro')
    upip.install('micropython-uasyncio.queues')


do_connect()
install_modules()