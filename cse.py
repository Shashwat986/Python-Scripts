import sys
import re
import urllib2
import urlparse
import time
from bs4 import BeautifulSoup

urls=["http://www.cse.iitk.ac.in/users/admissions/details.html","http://www.cse.iitk.ac.in/users/admissions/home.html","http://www.cse.iitk.ac.in/users/admissions/index.mtech.html","http://www.cse.iitk.ac.in/users/admissions/interview.mtech.html"]

try:
	user_agent = 'Shashwat-Python'
	
	headers={'User-Agent':user_agent,}
	msg0=[]
	for url in urls:
		request=urllib2.Request(url,None,headers)
		response = urllib2.urlopen(request)
		msg0.append(response.read())

except:
	print "Not able to open Google"
	sys.exit(1)
	


try:
	while True:
		try:
			msg=[]
			for url in urls:
				request=urllib2.Request(url,None,headers)
				response = urllib2.urlopen(request)
				msg.append(response.read())
		except:
			print "Unable to connect. Retying in 5 seconds"
			time.sleep(5)
			continue
		if msg == msg0:
			print "Same. Retrying in 5 seconds"
			time.sleep(5)
		else:
			chgs=list(set(msg0)-set(msg))
			for chg in chgs:
				print "This url has changed:", urls[msg0.index(chg)]
			print "Different!!! Quitting..."
			exit(0)
except:
	sys.exit(1)
