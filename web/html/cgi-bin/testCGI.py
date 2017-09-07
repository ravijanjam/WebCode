#!/usr/bin/python

print "Content-Type: text/html\n\n"
from time import gmtime, strftime
import subprocess

#import os
#print os.environ['HOME']

#print ("Content-Type: text/html\n\n")

currTime = strftime("%Y-%m-%d %H:%M:%S", gmtime())

#subprocess.call(["ls", "-l"])
print ("From Python works, testing 123")
print ("I am called at: ", strftime("%Y-%m-%d %H:%M:%S", gmtime()) )
#print (subprocess.call(["ls", "-l"]))

def testFunc(currTime):
	print "from the function testFunc", currTime
	#f = open("/tmp/output.txt", "a+")

	#f = open("home/ravi/web/html/output.txt", "a")
	#f = open("/tmp/output.txt", "a")
	f = open("/tmp/output.txt", "a")
	f.write("hello from python\n");
	f.write(str(currTime))
	print(f)
	f.close()
	#subprocess.call(["ls", "-l"])
	print "End of the function testFunc\n"

testFunc(currTime)
#subprocess.call(["ls", "-l"])
