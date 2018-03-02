from heap import Heap
from heapFEL import HeapFEL
from customer import Customer
from counter import Counter
import numpy as np



def runsim():
	###-----Simulation Begins-----###
	f = open('sampleOutput.txt', 'w')
	#f1 = open('infoProb.txt', 'w')
	# To start with, initialize the FEL and the bank queue first.
	queue = Heap()
	FEL = HeapFEL()

	# The bank will open for eight hours. The program will run until the close time.
	currentTime = 0
	arrivalTime = 0
	closeTime = 480 

	#Initialize the counters
	counter1 = Counter()
	counter2 = Counter()
	# The time it takes for the second customer to arrive
	# It follows the exponential distribution 
	nextTime = np.random.exponential(scale = 7)
	arrivalTime += nextTime

	#Initialize the first customer and put in the FEL
	customer = Customer(arrivalTime)
	FEL.insert(['arr', customer.timestamp, customer])
	currentTime += nextTime

	#Initialize the counting helper. 
	# i is number of loop, freei is number of free event, arri is number of arrive event
	i = 0
	freei = 0
	arri = 0
	VIPCount = 0

	maxqueue = 0

	# Keep on iterating until the bank closes
	while currentTime < closeTime:
		#print "*******This is the " + str(i) +" loop*******"
		i += 1
		#Get the event in the FEL with the smallest timestamp
		event = FEL.delMin()
		#print 'ts:', event[1]
		currentTime = event[1]

		#if it is an arrival event
		if event[0] == 'arr':
			arri += 1
			f.write("This is the " + str(arri) + " arrival\n")

			#If there is a counter that is not busy, the customer go to that counter
			#Then a "free" event with the timestamp a counter is available will be inserted to the FEL 
			if counter1.busyUntil < event[1]:
				counter1.busyUntil = currentTime + event[2].serveTime
				FEL.insert(['free1', counter1.busyUntil, counter1])
			elif counter2.busyUntil < event[1]:
				counter2.busyUntil = currentTime + event[2].serveTime
				FEL.insert(['free2', counter2.busyUntil, counter2])

			#If there is no counter available, the customer goes to the queue
			else:
				#If the customer is an VIP, he goes to the head of the queue diretly
				if event[2].isVIP:
					f.write('VIP detected\n')
					event[2].timestamp = VIPCount
					VIPCount += 1
				queue.insert(event[2])
				f.write("This customer went to the queue, queue length is " + str(len(queue.heapList) - 1) + "\n")
		if len(queue.heapList) > maxqueue:
			maxqueue = len(queue.heapList)

		#if the event is free, the find a customer from the queue to serve.
		elif event[0] == 'free1':
			freei += 1
			f.write("This is the " + str(freei) + " free\n")
			#if the queue is not empty, delete the customer with the smallest timestamp
			if queue.currentSize != 0:
				currCustomer = queue.delMin()
				f.write('A customer served by the counter, queue length is' + str(len(queue.heapList) - 1) +"\n")
				#The customer has a maximum time to wait. 
				#If the time waiting is more than the patience, the customer will leave, leaving the servetime 0.
				if currCustomer.timestamp + currCustomer.waitTime > currentTime:
					counter1.busyUntil = currentTime
					f.write('A customer quited from the queue\n')
				else:
					counter1.busyUntil = currentTime + currCustomer.serveTime
				FEL.insert(['free1', counter1.busyUntil, counter1])
		# The case of the other counter
		elif event[0] == 'free2':
			freei += 1
			f.write("This is the " + str(freei) + " free\n")
			if queue.currentSize != 0:
				currCustomer = queue.delMin()
				f.write('A customer served by the counter, queue length is' + str(len(queue.heapList) - 1) +"\n")
				counter2.busyUntil = currentTime + currCustomer.serveTime
				if currCustomer.timestamp + currCustomer.waitTime > currentTime:
					counter2.busyUntil = currentTime
					f.write('A customer quited from the queue\n')
				else:
					counter2.busyUntil = currentTime + currCustomer.serveTime
				FEL.insert(['free2', counter2.busyUntil, counter2])

		# Generate the next customer
		# Customers come with different frequency at different time
		if currentTime < 120:
			nextTime = np.random.exponential(scale = 8.42)
		elif currentTime < 420:
			nextTime = np.random.exponential(scale = 6.94)
		else:
			nextTime = np.random.exponential(scale = 12.63)
		arrivalTime += nextTime
		FEL.insert(['arr', arrivalTime, Customer(arrivalTime)])

	# If the bank is already closed but there are still some customers in the queue, they will be served 
	#Only counter 1 will open
	while queue.currentSize > 0:
		currentTime = counter1.busyUntil
		customer = queue.delMin()
		counter1.busyUntil = currentTime + customer.serveTime
		f.write('A customer is served after 5 p.m.')
	#f1.write(str(maxqueue) + ', ')
	#print maxqueue,
	f.close()

def main():
	runsim()

if __name__ == "__main__":
	main()



