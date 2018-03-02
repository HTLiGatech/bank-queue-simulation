import random
class Customer():
	def __init__(self, timestamp):
		#The posibility that the customer is VIP is 0.2
		self.isVIPProb = 0.2
		if random.random() < self.isVIPProb:
			self.isVIP = True
		else:
			self.isVIP = False
		#The posibility that the customer need information service is 0.8
		self.isInfoProb = 0.6
		if random.random() < self.isInfoProb:
			self.serveTime = random.uniform(3,7)
		else:
			self.serveTime = random.uniform(20,30)
		#Waiting patience. The Customer will leave if the time for waiting is too long.
		self.waitTime = random.uniform(30, 60)
		#The time the customer comes
		self.timestamp = timestamp


