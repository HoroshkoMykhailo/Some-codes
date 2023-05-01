import sys

class H:
    def __init__(self):
        self.size = 0
        self.A = []
        
    def parent(self, i):
        return (i - 1)//2 
    
    def left(self, i):
        return 2*i + 1
    
    def right(self, i):
        return 2*i + 2

    def getsize(self):
        return self.size
    
class Hhigh(H):
    
    def __init__(self):
        super().__init__()
    
    def decreaseKey(self, i, key):
        self.A[i] = key
        while(i > 0 and self.A[self.parent(i)] > self.A[i]):
            temp = self.A[i]
            self.A[i] = self.A[self.parent(i)]
            self.A[self.parent(i)] = temp
            i = self.parent(i)
            
    def insert(self, key):
        self.size = self.size + 1
        self.A.append(0)
        self.decreaseKey(self.size - 1, key)
        
    def minimum(self):
        return self.A[0]

    def minHeapify(self, i):
        p = self.left(i)
        q = self.right(i)
        if p < self.size and self.A[p] < self.A[i]:
            smallest = p
        else:
            smallest = i
        if q < self.size and self.A[q] < self.A[smallest]:
            smallest = q
        if smallest != i:
            temp = self.A[i]
            self.A[i] = self.A[smallest]
            self.A[smallest] = temp
            self.minHeapify(smallest)
        
    def extractMin(self):
        minim = self.A[0]
        self.A[0] = self.A[self.size - 1]
        self.A.pop(self.size - 1)
        self.size = self.size - 1
        self.minHeapify(0)
        return minim
        
class Hlow(H):
    
    def __init__(self):
        super().__init__()
    
    def increaseKey(self, i, key):
        self.A[i] = key
        while(i > 0 and self.A[self.parent(i)] < self.A[i]):
            temp = self.A[i]
            self.A[i] = self.A[self.parent(i)]
            self.A[self.parent(i)] = temp
            i = self.parent(i)
            
    def insert(self, key):
        self.size = self.size + 1
        self.A.append(0)
        self.increaseKey(self.size - 1, key)
        
    def maximum(self):
        return self.A[0]
    
    def maxHeapify(self, i):
        p = self.left(i)
        q = self.right(i)
        if p < self.size and self.A[p] > self.A[i]:
            largest = p
        else:
            largest = i
        if q < self.size and self.A[q] > self.A[largest]:
            largest = q
        if largest != i:
            temp = self.A[i]
            self.A[i] = self.A[largest]
            self.A[largest] = temp
            self.maxHeapify(largest)
        
    def extractMax(self):
        maxim = self.A[0]
        self.A[0] = self.A[self.size - 1]
        self.A.pop(self.size - 1)
        self.size = self.size - 1
        self.maxHeapify(0)
        return maxim
        
fname = sys.argv[1]
file = open(fname, "r")
N = int(file.readline())
out = 'ip_21_Horoshko_05_output_' + str(N) + '.txt'
f = open(out, "w")
Plow = Hlow()
Phigh = Hhigh()
ar = [0]*N
for i in range(N):
    ar[i] = int(file.readline())
    if i == 0:
        med = str(ar[0])
        Plow.insert(ar[0])
    elif i == 1:
        med = str(ar[0]) + ' ' + str(ar[1])
        if(ar[i] < Plow.maximum()):
            Plow.insert(ar[i])
        else:
            Phigh.insert(ar[i])
    else:
        if(ar[i] < Plow.maximum()):
            Plow.insert(ar[i])
        else:
            Phigh.insert(ar[i])
        if(Plow.getsize() - Phigh.getsize() > 1):
            Phigh.insert(Plow.extractMax())
        if(Phigh.getsize() - Plow.getsize() > 1):
            Plow.insert(Phigh.extractMin())
        if( i % 2 == 0):
            if(Phigh.size > Plow.size):
                med = str(Phigh.minimum())
            else:
                med = str(Plow.maximum())
        else:
            med = str(Plow.maximum()) + ' ' + str(Phigh.minimum())
    med = med + '\n'
    f.write(med)             
file.close()
f.close()
