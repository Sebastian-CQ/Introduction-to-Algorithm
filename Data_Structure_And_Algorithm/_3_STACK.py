class Stack:
    # 基于list实现，list左端为stack底端
    def __init__(self, item=None):
        if type(item) == list:
            self.items = item
        elif item is None:
            self.items = []
        else:
            self.items = [item]

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


class Stack2:
    # 基于list实现，list右端为顶端
    def __init__(self, item=None):
        if type(item) == list:
            self.items = item
        else:
            self.items = [item]

    def is_empty(self):
        return self.items is []

    def size(self):
        return len(self.items)

    def push(self, item):
        # items = self.items
        # self.items = [item]
        # for i in range(self.size()):
        #     self.items.append(items[i])
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]


def parChecker(symbols):
    # 本算法只判断同类符号
    s = Stack()
    match = True
    for i in range(len(symbols)):
        symbol = symbols[i]
        if symbol == '(':
            s.push(symbol)
        else:
            if s.is_empty():
                match = False
                break
            else:
                s.pop()
    if match and s.is_empty():
        return True
    else:
        return False


def parChecher_all(symbols):
    s = Stack()
    match = True
    index = 0
    while index < len(symbols) and match:
        symbol = symbols[index]
        if symbol in '([{':
            s.push(symbol)
        else:
            if s.is_empty():
                match = False
            left = s.pop()
            if not matches(left, symbol):
                match = False
        index += 1
    return match


def matches(left, right):
    opens = '([{'
    closes = ')]}'
    return opens.index(left) == closes.index(right)


def transform(num, base):
    # 10进制转换
    if type(num) != int:
        return TypeError
    if base == 2:
        digits = '01'
    elif base == 8:
        digits = '01234567'
    elif base == 17:
        digits = '01234567ABCDEF'

    s = Stack()
    while num > 0:
        rem = num % base
        s.push(rem)
        num = num // base

    new_num = ''
    while not s.is_empty():
        new_num = new_num + digits[s.pop()]
    return new_num


def infixToPostifix(infixexper):
    prec = {'(': 1,
            '+': 2,
            '-': 2,
            '*': 3,
            '/': 3}
    opstack = Stack()
    postfixList = []
    tokenList = infixexper.split()
    for token in tokenList:
        if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or token in '0123456789':
            postfixList.append(token)
        elif token == '(':
            opstack.push(token)
        elif token == ')':
            toptoken = opstack.pop()
            while toptoken != '(':
                postfixList.append(toptoken)
                toptoken = opstack.pop()
        else:
            while (not opstack.is_empty()) and prec[opstack.peek()] >= prec[token]:
                postfixList.append(opstack.pop())
            opstack.push(token)
    while not opstack.is_empty():
        postfixList.append(opstack.pop())
    return ' '.join(postfixList)


def computePostfix(postfix):
    stack = Stack()
    postList = postfix.split()
    print(postList)
    for token in postList:
        if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or token in '0123456789':
            stack.push(int(token))
        else:
            a = stack.pop()
            b = stack.pop()
            stack.push(compute(a, b, token))
    if stack.size() == 1:
        return stack.pop()


def compute(a, b, token):
    if token == '+':
        return a + b
    elif token == '-':
        return a - b
    elif token == '*':
        return a * b
    elif token == '/':
        return a / b


# list = infixToPostifix('1 + 2 + 3')
# print(list)
# print(computePostfix(infixToPostifix('1 + 2 + 3')))








