class BinaryHeap:
    def __init__(self):
        self.heapList = [0]
        self.Size = 0

    def bulidHeap(self, alist):
        length = len(alist)
        self.Size = length
        self.heapList = [0] + alist
        i = length
        while i > 0 :
            self.MaxHeapify(i)
            i -= 1
        print('Creating Binary Heap complete')

    def MaxHeapify(self, i):
        while i * 2 <= self.Size:
            maxChild = self._MaxChild(i)
            if self.heapList[maxChild] > self.heapList[i]:
                self.heapList[i], self.heapList[maxChild] = self.heapList[maxChild], self.heapList[i]
            i = maxChild

    def _MaxChild(self, i):
        if 2 * i + 1 > self.Size:
            return 2 * i
        else:
            if self.heapList[2*i+1] > self.heapList[2*i]:
                return 2*i+1
            else:
                return 2*i

    def sort(self):
        pre_List = self.heapList.copy()
        sorted_List = []
        while self.Size > 0:
            self.heapList[1], self.heapList[-1] = self.heapList[-1], self.heapList[1]
            sorted_List.append(self.heapList.pop())
            self.Size -= 1
            self.MaxHeapify(1)
        self.bulidHeap(pre_List)
        print('Sort List complete')
        return sorted_List

    # 最大堆实现最大优先队列
    def Maximum(self):
        return self.heapList[1]

    def Extract_Max(self):
        self.heapList[1], self.heapList[-1] = self.heapList[-1], self.heapList[1]
        self.heapList.pop()
        self.MaxHeapify(1)

    def Insert(self, key):
        self.heapList.append(key)
        self.Size += 1
        self._insert_Up(self.Size)
        print('Insertion complete')

    def _insert_Up(self, i):
        while i // 2 > 0:
            if self.heapList[i] > self.heapList[i//2]:
                self.heapList[i], self.heapList[i // 2] = self.heapList[i//2], self.heapList[i]
            else:
                break
            i = i // 2


bh = BinaryHeap()
bh.bulidHeap([5, 10, 19, 23, 1, 7, 8])
bh.Insert(9)
print(bh.sort())

