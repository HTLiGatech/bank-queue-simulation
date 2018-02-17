class HeapFEL:
    def __init__(self):
        self.heapList = [[0,0,0]]
        self.currentSize = 0
 
    def insert(self,k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        i = self.currentSize
        while i // 2 > 0:
            if self.heapList[i][1] < self.heapList[i // 2][1]:
                self.heapList[i // 2], self.heapList[i] = self.heapList[i], self.heapList[i // 2]
            i = i // 2
 
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
                if self.heapList[i*2][1] < self.heapList[i*2+1][1]:
                    mc = i * 2
                else:
                    mc = i * 2 + 1
            if self.heapList[i][1] > self.heapList[mc][1]:
                self.heapList[i], self.heapList[mc] = self.heapList[mc], self.heapList[i]
            i = mc
        return retval
 

    def printHeap(self):
        for index, event in enumerate(self.heapList):
            for item in event:
                print item
            print '**********'
