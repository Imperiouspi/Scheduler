import os.path
import datetime
import time
import sys

def printtime():
	return time.strftime("%Y-%m-%d (%H:%M:%S)")

def analyze(read):
	if '- 01:30' in read:
		print 'read'
	return read

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
schedule.write("Noah's Schedule" + " " + printtime())

events_tom = ["\nArrive Home\n"]
events_proj = []
tomorrow = True
for line in todo:
	if(line == "Projects\n"):
			tomorrow = False

	if((line != "Due Tomorrow\n") and (line !="") and (line != "Projects\n") and (line !="\n")):
		appender = analyze(line)
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
