class BinaryHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    # 插入操作
    def _percUp(self, i):
        # 将新的key上浮到合适的位置
            while i // 2 > 0:
                if self.heapList[i] < self.heapList[i//2]:
                    self.heapList[i], self.heapList[i//2] = self.heapList[i//2], self.heapList[i]
                i = i // 2

    def inset(self, k):
        self.heapList.append(k)
        self.currentSize += 1
        self._percUp(self.currentSize)

    # 移除操作，移除最小的DelMin()
    def DelMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[-1]
        self.heapList.pop()
        self._percDown(1)
        return retval

    def _percDown(self, i):
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

    # 从list使用下沉法生产堆， 复杂度O（n）
    def buildHeap(self, alist):
        i = len(alist)
        self.heapList = [0] + alist
        self.currentSize = len(alist)
        print(alist, i)
        while i > 0:
            self._percDown(i)
            i -= 1
        print(self.heapList, i)

    # 堆排序，使用二叉堆，复杂度为O（n），每次将第一个数和最后一个数交换，把最后一个数pop，整理二叉堆，重复上述操作
    def sort(self):
        sortedList = []
        while self.currentSize >= 1:
            self.heapList[1], self.heapList[self.currentSize] = self.heapList[self.currentSize], self.heapList[1]
            sortedList.append(self.heapList.pop())
            self.currentSize -= 1
            self._percDown(1)
        return sortedList


blist = [7, 15, 1, 3, 9, 11, 2, 19, 23, 20]
bh = BinaryHeap()
bh.buildHeap(blist)
print(bh.sort())

