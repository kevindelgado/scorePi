from Adafruit_CharLCD import Adafruit_CharLCD
import os
import time

lcd = Adafruit_CharLCD()

cmd = "node scraper.js > game_text.txt"

#f_name = "game_text.txt"

lcd.begin(16,1)

print "running cmd"
os.system(cmd)
print "waiting 5 seconds"
time.sleep(5)
print "finished waiting, killing terminal"
os.system("^C")

list = []
f = open("game_text.txt")
print "reading list"
for line in f:
	list += [line]
f.close()

def format_line(line):
	if len(line) > 15:
		line_arr = line.split(' ')
		out_line = '';
		for l in range(0,len(line_arr)):
			if len(line_arr[l]) > 5:
				out_line += line_arr[l][:5]
			else:
				out_line += line_arr[l]
			out_line += ' '
		return out_line
	return line
while 1:				
	for i in range(0,len(list),2):
		lcd.clear()
		cur_line = list[i]
		next_line = list[i+1]
		cur_line = format_line(cur_line)
		print cur_line
		lcd.message('%s\n' % cur_line)
		next_line = format_line(next_line)
		print next_line
		lcd.message('%s' % next_line)
		time.sleep(3)

