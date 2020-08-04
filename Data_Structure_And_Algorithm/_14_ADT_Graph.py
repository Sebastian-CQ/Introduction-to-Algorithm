class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        self.color = 'white'

    def addNeighbor(self, neighbor, weight=0):
        self.connectedTo[neighbor] = weight

    def __str__(self):
        return str(self.id) + 'connectedTo' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, neighbor):
        return self.connectedTo[neighbor]

    def setColor(self, Str):
        self.color = Str

    def getColor(self):
        return self.color


class Graph:
    def __init__(self):
        self.vertexList = {}
        self.nimVertices = 0

    def addVertex(self, key):
        self.nimVertices += 1
        currentVertex = Vertex(key)
        self.vertexList[key] = currentVertex
        # return currentVertex

    def getVertex(self, key):
        if key in self.vertexList:
            return self.vertexList[key]
        else:
            return None

    def __contains__(self, key):
        return key in self.vertexList

    def addEdge(self, f, t, cost=0):
        if f not in self.vertexList:
            self.addVertex(f)
        if t not in self.vertexList:
            self.addVertex(t)
        self.vertexList[f].addNeighbor(self.vertexList[t], cost)

    def getVertices(self):
        return self.vertexList.keys()

    def __iter__(self):
        return iter(self.vertexList.values())


# 得到合法的下一步
def genLegalMoves(x, y, bdSize):
    newMoves = []
    moveOffsets = [(-1, -2), (-1, 2), (-2, -1), (-2, 1),
                   (1, -2), (1, 2), (2, -1), (2, 1)]
    for i in moveOffsets:
        newX = x + i[0]
        newY = y + i[1]
        if legalCoord(newX, bdSize) and legalCoord(newY, bdSize):
            newMoves.append((newX, newY))
    return newMoves


def legalCoord(x, bdSize):
    if 0 <= x < bdSize:
        return True
    else:
        return False


# 添加棋盘
def knightGraph(bdSize):
    ktGraph = Graph()
    for row in range(bdSize):
        for col in range(bdSize):
            nodeId = posToNodeId(row, col, bdSize)
            newPositions = genLegalMoves(row, col, bdSize)
            for e in newPositions:
                nid = posToNodeId(e[0], e[1], bdSize)
                ktGraph.addEdge(nodeId, nid)

    return ktGraph


def posToNodeId(x, y, bdSize):
    return x * bdSize + y


# 开始骑士周游
def knightTour(n, path, u, limit):
    u.setColor('gray')
    path.append(u)
    if n < limit:
        nbrList = list(u.getConnections())
        i = 0
        done = False
        while i < len(nbrList) and not done:
            if nbrList[i].getColor() == 'white':
                done = knightTour(n+1, path, nbrList[i], limit)
            i += 1
        if not done:
            path.pop()
            u.setColor('white')
    else:
        done = True
    if n == limit - 1:
        print(path)
        print(len(path))
    return done


graph = knightGraph(bdSize=5)
n = 1
limit = 25
path = []
knightTour(n, path, u=graph.getVertex(1), limit=limit)



