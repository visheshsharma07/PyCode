import logging
import second
import requests
import urllib2
import time
import backoff

# for logging all the data into test.log file
logging.basicConfig(filename="test.log",level=logging.INFO,format="%(asctime)s:%(levelname)s:%(message)s")

@backoff.on_exception(backoff.expo,requests.exceptions.Timeout, max_value = 1, max_tries = 10)
def requests_retry():
	logging.info("In the function")
	print "Running"
	return requests.get('http://127.0.0.1:4040/',timeout=1)


if __name__ == "__main__":
	logging.info(time.time())
	try:
		r = requests_retry()
		logging.info(r.text)
	except BaseException,e:
		print e	
	logging.info("Currently in first.py")
	logging.info(second.randomCal(40000))
	print "Completed here"
	logging.info(time.time())
