class BinaryHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def Max_Heapify(self, i):
        while (i * 2) <= self.currentSize:
            MinChild = self.minchild(i)
            if self.heapList[i] > self.heapList[MinChild]:
                self.heapList[i], self.heapList[MinChild] = self.heapList[MinChild], self.heapList[i]
            i = MinChild

    def minchild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i*2
        else:
            if self.heapList[i*2] < self.heapList[i*2 + 1]:
                return i*2
            else:
                return i*2 + 1

    def buildHeap(self, alist):
        i = len(alist)
        self.heapList = [0] + alist
        self.currentSize = len(alist)
        while i > 0:
            self.Max_Heapify(i)
            i -= 1
        print('创建二叉堆完成')

    def sort(self):
        sortedList = []
        while self.currentSize >= 1:
            self.heapList[1], self.heapList[self.currentSize] = self.heapList[self.currentSize], self.heapList[1]
            sortedList.append(self.heapList.pop())
            self.currentSize -= 1
            self.Max_Heapify(1)
        return sortedList

    # 最小堆实现最小优先队列
    def Minimum(self):
        return self.heapList[1]

    def Extract_Min(self):
        min = self.heapList[1]
        self.heapList[1], self.heapList[-1] = self.heapList[-1], self.heapList[1]
        self.currentSize -= 1
        self.Max_Heapify(1)
        return min

    def Insert(self, key):
        self.currentSize += 1
        self.heapList.append(key)
        self._insert_Up(self.currentSize)
        print('插入完成')

    def _insert_Up(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i//2]:
                self.heapList[i], self.heapList[i//2] = self.heapList[i//2], self.heapList[i]
            i = i // 2


bh = BinaryHeap()
bh.buildHeap([5, 10, 19, 23, 1, 7, 8])
print(bh.heapList)
bh.Extract_Min()
print(bh.sort())
