#!/usr/bin/python
import os


domains = ['www.allenservice.ga','www.castmart.ga', 'stngpetty.ga', 'ggautosrep.ga', 'google.com']

for i in domains:
	response = os.system("ping -c 1 " + i + "> /dev/null 2>&1")
	if response == 0:
  		print i, 'is up!'
  		os.system("proxychains wget " + i + "> " + i +".txt")
	else:
  		print i, 'is down!'