class Node:
    def __init__(self, initial):
        self.data = initial
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newData):
        self.data = newData

    def setNext(self, newNext):
        self.next = newNext


class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        size = 0
        current = self.head
        while current is not None:
            size += 1
            current = current.getNext()
        return size

    def search(self, target):
        search = False
        current = self.head
        while current is not None and not search:
            if current.getData() == target:
                search = True
            else:
                current = current.getNext()
        return search

    def remove(self, item):
        if self.search(item):
            current = self.head
            while True:
                if current.getNext().getData() == item:
                    current.setNext(current.getNext().getNext())
                    break
                current = current.getNext()

    def traversal(self):
        traversal_list = []
        current = self.head
        while current is not None:
            traversal_list.append(current.getData())
            current = current.getNext()

        return traversal_list


class OrderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def size(self):
        size = 0
        current = self.head
        while current is not None:
            size += 1
            current = current.getNext()
        return size

    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current is not None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()

        return found

    def add(self, item):
        current = self.head
        node = Node(item)
        previous = None
        stop = False
        while current is not None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()
        if previous is None:
            node.setNext(self.head)
            self.head = node
        else:
            node.setNext(current)
            previous.setNext(node)

    def remove(self, item):
        if not self.search(item):
            return
        current = self.head
        previous = None
        while current.getData() != item:
            previous = current
            current = current.getNext()
        previous.setNext(current.getNext())

    def traverlsal(self):
        traverl_List = []
        current = self.head
        while current is not None:
            traverl_List.append(current.getData())
            current = current.getNext()

        return traverl_List


o_list = OrderedList()
o_list.add(1)
print(o_list.traverlsal())
o_list.add(5)
o_list.add(10)
o_list.add(15)
print(o_list.traverlsal())
o_list.remove(10)
print(o_list.traverlsal())






