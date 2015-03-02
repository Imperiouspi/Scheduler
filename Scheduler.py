import os.path
import datetime
import time
import sys
import re
from datetime import timedelta

StartTime = datetime.timedelta(minutes = int(time.strftime("%M")), hours = int(time.strftime("%H")))
NowTime = StartTime
Adjuster = datetime.timedelta(minutes = 0, hours = 12)
if int(time.strftime("%H")) > 12:
	NowTime = NowTime - Adjuster

def printtime():
	date = time.strftime("%a %b %d, %Y (%H:%M)")
	if int(time.strftime("%H")) > 12:
		Hours = int(time.strftime("%H"))-12
		date = time.strftime("%a %b %d, %Y (" + str(Hours) + ":%M)")
	return date

def analyze(read):
	topic = "OOPS"
	if re.match('.* - [0-2][0-9]:[0-5][0-9]\n', read):
		print "Timed: " + read
		found = re.search('.* (?=- [0-2][0-9]:[0-5][0-9])', read)
		time = re.search('[0-2][0-9]:[0-5][0-9]', read)
		topic = found.group(0) + "\n"
	if topic == "OOPS":
		return read, topic
	else:
		return topic, time.group(0)

def findTimeScheduled(timeScheduled, topic):
	global NowTime
	hourTime = re.search('.*(?=:[0-5][0-9])', timeScheduled)
	hourTime = hourTime.group(0)
	
	minuteTime = re.search('(?<=[0-5][0-9]:).*', timeScheduled)
	minuteTime = minuteTime.group(0)
	
	time = str(NowTime)
	time = time[:-3]
	print(time)

	timeScheduled = datetime.timedelta(minutes = int(minuteTime), hours = int(hourTime))
	NowTime = timeSlot(NowTime, timeScheduled)
	
	return time + " " + topic

def timeSlot(last, length):
	return (last + length)
def addEvent(appendee, breaker):
	events_tom.append(appender)
	events_tom.append(breaker)
if sys.platform == 'darwin':
	fileprefix = '/Users/Noah/Workspaces/Scheduler/'
	schedule = open(fileprefix + 'schedule.txt','w')

	if(not(os.path.isfile(fileprefix + 'ToDo.txt'))):
		todo = open(fileprefix + 'ToDo.txt','w')

	todo = open(fileprefix + 'ToDo.txt','r')
else:
	fileprefix = 'H:\Python\\'
	schedule = open(fileprefix + 'schedule.txt','w')

	if(not(os.path.isfile(fileprefix + 'ToDo.txt'))):
		todo = open(fileprefix + 'ToDo.txt','w')

	todo = open(fileprefix + 'ToDo.txt','r')

#Header
schedule.write("Noah's Schedule:" + " " + printtime())

events_tom = ["\n"]
events_proj = []
tomorrow = True
breakTime = ""

for line in todo:
	if(line == "Projects\n"):
			tomorrow = False

	if((line != "Due Tomorrow\n") and (line !="") and (line != "Projects\n") and (line !="\n")):
		appender, topicTime = analyze(line)
		if topicTime != "OOPS":
			appender = findTimeScheduled(topicTime, appender)
		else:
			appender = findTimeScheduled("01:30", appender)

		breakTime = findTimeScheduled("00:15", "Break\n")

		if(tomorrow):
			addEvent(appender, breakTime)
		else:
			#addProject()
			events_proj.append(appender)
events_proj.append("\n" + str(NowTime)[:-3] + " Go to Bed!")
for i in events_tom:
	schedule.write(i)

for i in events_proj:
	schedule.write(i)

schedule.close()
todo.close()
