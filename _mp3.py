#!/usr/bin/python

from subprocess import call
import subprocess
import sys

def play_sound( filename ):
   call(["./pifm", filename])


def play_mp3(filename, freq=100.0):
	#call(["avconv", "-i", filename, "-f", "s16le", "-ar", "22.05k", "-ac", "1", "-", "|", "sudo", "./pifm", "-", str(freq)])
	p1 = subprocess.Popen(["avconv", "-i", filename, "-f", "s16le", "-ar", "22.05k", "-ac", "1", "-"], stdout=subprocess.PIPE) #Set up the echo command and direct the output to a pipe
	p2 = subprocess.Popen(["sudo", "./pifm", "-", str(freq)], stdin=p1.stdout) #send p1's output to p2
	p1.stdout.close() #make sure we close the output so p2 doesn't hang waiting for more input
	output = p2.communicate()[0] #run our commands



if len(sys.argv) == 1:
	print 'usage : python pifm_mp3.py filename [freq]'
if len(sys.argv) == 2:
	play_mp3(sys.argv[1])
if len(sys.argv) == 3:
	play_mp3(sys.argv[1], sys.argv[2])


