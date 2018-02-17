from customer import Customer
class Heap:
    #Initialize the heap
    def __init__(self):
        self.heapList = [Customer(0)]
        self.currentSize = 0
    
    #insert a item into the heap
    def insert(self,k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        i = self.currentSize
        while i // 2 > 0:
            if self.heapList[i].timestamp < self.heapList[i // 2].timestamp:
                self.heapList[i // 2], self.heapList[i] = self.heapList[i], self.heapList[i // 2]
            i = i // 2

    # Find the place of the child with minumum timestamp
    def minChild(self,i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2].timestamp < self.heapList[i*2+1].timestamp:
                return i * 2
            else:
                return i * 2 + 1
 
    #Delete the item with the minimum timestamp and return it
    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        i = 1
        while (i * 2) <= self.currentSize:
            if i * 2 + 1 > self.currentSize:
                mc = i * 2
            else:
                if self.heapList[i*2].timestamp < self.heapList[i*2+1].timestamp:
                    mc = i * 2
                else:
                    mc =  i * 2 + 1
            if self.heapList[i].timestamp > self.heapList[mc].timestamp:
                self.heapList[i], self.heapList[mc] = self.heapList[mc], self.heapList[i]
            i = mc
        return retval

    # Print what exactly is in the heap. For testing. 
    def printHeap(self):
        for index, customer in enumerate(self.heapList):
            print '*******Customer' + str(index) + '*******' 
            print 'timestamp' + str(customer.timestamp)
            print 'wait time:' + str(customer.waitTime)
            print 'service time' + str(customer.serveTime)