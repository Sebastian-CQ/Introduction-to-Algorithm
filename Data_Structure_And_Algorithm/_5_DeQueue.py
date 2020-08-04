class DeQueue:
    def __init__(self):
        self.items = []

    def addFront(self, item):
        self.items.insert(0, item)

    def addRear(self, item):
        self.items.append(item)

    def removeFront(self):
        return self.items.pop(0)

    def removeRear(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)


def palChecker(String):
    # 判断字符串是否为回文词
    strDequeue = DeQueue()
    for ch in String:
        strDequeue.addRear(ch)

    match = True
    while strDequeue.size() >= 2:
        str_Front = strDequeue.removeFront()
        str_Rear = strDequeue.removeRear()
        if str_Front is not str_Rear:
            match = False
            break

    return match

print(palChecker('FronttnorF'))

