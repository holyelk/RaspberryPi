#!/usr/bin/python
import sys,re
import Adafruit_DHT
import os, csv
import time, threading
from time import sleep
from datetime import date

#15 Minutes
WAIT_SECONDS = 900

def truncate(num):
    return re.sub(r'^(\d+\.\d{,2})\d*$',r'\1',str(num))

def get_temp_hum():
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)
    #print(humidity," + ",temperature)
    return (humidity, temperature)

def get_date_now():
    today = date.today()
    return(today.strftime("%d/%m/%Y"))

def get_time_now():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    return(current_time)

def write_to_csv():
    # the a is for append, if w for write is used then it overwrites the file
    with open("/home/pi/sensor_readings.csv", mode="a") as sensor_readings:
        hum,temp = get_temp_hum()
        hum = truncate(hum)
        temp = truncate(temp)
        sensor_write = csv.writer(sensor_readings, delimiter=",", quotechar="\"", quoting=csv.QUOTE_MINIMAL)
        write_to_log = sensor_write.writerow([get_date_now(),get_time_now(),temp,hum])
        return(write_to_log)

def repeater():
    write_to_csv()
    threading.Timer(WAIT_SECONDS, repeater).start()

repeater()

        

