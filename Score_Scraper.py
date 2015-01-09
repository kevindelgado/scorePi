#!/usr/bin/python

from Adafruit_CharLCD import Adafruit_CharLCD
from subprocess import *
from time import sleep, strftime
#rom datetime import datetime

lcd = Adafruit_CharLCD()

#cmd= "ip addr show eth0 | grep inet | awk '{print $2}' | cut -d/ -f1"
cmd_str = "sudo node scraper.js "
cur = 9

lcd.begin(16, 1)

print "done_setup..."
def run_cmd(cmd):
    p = Popen(cmd, shell=True, stdout=PIPE)
    print "print p: %s" % (p)
    output = p.communicate()[0]
    print "output: %s" % (output)
    return output

while 1:
    print "clearing lcd"
    lcd.clear()
    print "lcd clear"
    cur_str = "%d" % (cur)
    print "cur_str: %s" % (cur_str)
    cmd = cmd_str + cur_str
    print "running cmd: %s" % (cmd)
    ipaddr = run_cmd(cmd)
    #cd.message(datetime.now().strftime('%b %d  %H:%M:%S\n'))
    #cd.message('IP %s' % (ipaddr))
    print ipaddr
    lcd.message('%s' % (ipaddr))
    print "updating cur"
    cur = cur + 1
    sleep(2)
    print "looping"
