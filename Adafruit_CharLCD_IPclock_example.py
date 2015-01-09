#!/usr/bin/python

from Adafruit_CharLCD import Adafruit_CharLCD
from subprocess import *
from time import sleep, strftime
#rom datetime import datetime

lcd = Adafruit_CharLCD()

#cmd= "ip addr show eth0 | grep inet | awk '{print $2}' | cut -d/ -f1"
cmd_str = "sudo node scraper.js "
cur = 2

lcd.begin(16, 1)


def run_cmd(cmd):
    p = Popen(cmd, shell=True, stdout=PIPE)
    output = p.communicate()[0]
    return output

while 1:
    lcd.clear()
    cmd = cmd_str + cur
    ipaddr = run_cmd(cmd)
    #cd.message(datetime.now().strftime('%b %d  %H:%M:%S\n'))
    #cd.message('IP %s' % (ipaddr))
    lcd.message('%s' % (ipaddr))
    cur = cur + 1
    sleep(2)
