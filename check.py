#!/usr/bin/python
import os

#add your domains in here
domains = ['']
#this will download the pages in question and place them in your current directory
for i in domains:
	response = os.system("ping -c 1 " + i + "> /dev/null 2>&1")
	if response == 0:
  		print i, 'is up!'
  		os.system("proxychains wget " + i + "> " + i +".txt")
	else:
  		print i, 'is down!'
