from datetime import datetime
from time import sleep
from sense_hat import SenseHat
#from sense_emu import SenseHat

from thi import *
from ifttt import Webhook

sense = SenseHat()

IFTTT_KEY = ''  # @param {type:"string"}
webhook = Webhook('demo', IFTTT_KEY)
prev_level = 0

while True:
    # Get sense data
    hum = sense.get_humidity()
    temp = sense.get_temperature()
    thi = get_thi(temp, hum)
    level = get_thi_level(thi)
    print(datetime.now())
    print("Humidity: %s %%rH" % hum)
    print("Temperature: %s C" % temp)
    print("TH-index:", thi)
    print("TH-Level:", level)

    # IFTTT Webhook
    if prev_level < 4 and level >= 4:
        webhook.post(event='turn_on')
        print('Turn On!!')
    elif prev_level >= 4 and level < 4:
        webhook.post(event='turn_off')
        print('Turn Off')

    # Save prev level
    prev_level = level
    # Interval
    sleep(5)
