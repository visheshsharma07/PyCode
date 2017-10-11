import logging

logging.basicConfig(filename="test.log",level=logging.INFO,format="%(asctime)s:%(levelname)s:%(message)s")

def randomCal(n):
	logging.info("Currently in second.py")
	result = (n**2)/6
	return result