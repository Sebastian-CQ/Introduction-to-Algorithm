import random


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def en_queue(self, item):
        self.items.append(item)

    def de_queue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


def hot_Potato(namelist, num):
    # 现代版击鼓传花，或热土豆问题
    simulate = Queue()
    for name in namelist:
        simulate.en_queue(name)

    while simulate.size() > 1:
        for i in range(num):
            name = simulate.de_queue()
            simulate.en_queue(name)
        simulate.de_queue()
    return simulate.de_queue()


class Print:
    def __init__(self, ppm):
        self.pagerate = ppm     # 打印速度
        self.currentTask = None     # 正在打印任务
        self.timeRemaining = 0

    def tick(self):
        if self.currentTask is not None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        # 检查打印是否繁忙
        if self.currentTask is not None:
            return True
        else:
            return False

    def startNext(self, new_task):
        self.currentTask = new_task
        self.timeRemaining = new_task.get_Pages() * 60 / self.pagerate


class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def get_Stamp(self):
        return self.timestamp

    def get_Pages(self):
        return self.pages

    def wait_time(self, currenttime):
        return currenttime - self.timestamp


def newPrintTask():
    num = random.randrange(0, 180)
    if num == 1:
        return True
    else:
        return False


def simulation(numSecond, pagesPerMinute):
    labprinter = Print(pagesPerMinute)
    printQueue = Queue()
    waitingtime = []

    for currenttime in range(numSecond):
        if newPrintTask():
            task = Task(currenttime)
            printQueue.en_queue(task)

        if (not labprinter.busy()) and (not printQueue.is_empty()):
            nexttask = printQueue.de_queue()
            waitingtime.append(nexttask.wait_time(currenttime))
            labprinter.startNext(nexttask)

        labprinter.tick()

    averageWaitingtime = sum(waitingtime) / len(waitingtime)
    print('Average waiting time %6.2f secs , %3d task remaining' %(averageWaitingtime, printQueue.size()))


for i in range(10):
    simulation(3600, 5)
