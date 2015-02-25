import os.path
import datetime
import time
import sys
import re
from datetime import timedelta

def printtime():
	return time.strftime("%a %b %d, %Y (%H:%M:%S)")

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

def findTimeSlot(timeScheduled, topic):
	hourTime = re.search('.*(?=:[0-5][0-9])', timeScheduled)
	hourTime = hourTime.group(0)
	
	minuteTime = re.search('(?<=[0-5][0-9]:).*', timeScheduled)
	minuteTime = minuteTime.group(0)
	
	timeScheduled = datetime.timedelta(minutes = int(minuteTime), hours = int(hourTime))
	time = str(timeScheduled)

	time = time[:-3]
	print time
	return time + " " + topic

def giveTimeSlot(topic):
	return "1:30 " + topic

if sys.platform == 'darwin':
	fileprefix = '/Users/Noah/Workspaces/Scheduler/'
	schedule = open(fileprefix + 'schedule.txt','w')

	if(not(os.path.isfile(fileprefix + 'ToDo.txt'))):
		todo = open(fileprefix + 'ToDo.txt','w')

	todo = open(fileprefix + 'ToDo.txt','r')
else:
	fileprefix = 'H:\Python'
	schedule = open(fileprefix + 'schedule.txt','w')

	if(not(os.path.isfile(fileprefix + 'ToDo.txt'))):
		todo = open(fileprefix + 'ToDo.txt','w')

	todo = open(fileprefix + 'ToDo.txt','r')

#Header
schedule.write("Noah's Schedule:" + " " + printtime())

events_tom = ["\nBegin Work\n"]
events_proj = []
tomorrow = True
for line in todo:
	if(line == "Projects\n"):
			tomorrow = False

	if((line != "Due Tomorrow\n") and (line !="") and (line != "Projects\n") and (line !="\n")):
		appender, topicTime = analyze(line)
		if topicTime != "OOPS":
			appender = findTimeSlot(topicTime, appender)
		else:
			appender = giveTimeSlot(appender)
		if(tomorrow):
			events_tom.append(appender)
		else:
			events_proj.append(appender)

for i in events_tom:
	schedule.write(i)

for i in events_proj:
	schedule.write(i)

schedule.close()
todo.close()
