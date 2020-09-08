from datetime import datetime
from time import sleep
from sense_hat import SenseHat
#from sense_emu import SenseHat

from thi import *

sense = SenseHat()

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

    # Interval
    sleep(5)
