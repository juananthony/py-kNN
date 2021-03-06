from PyKMeansPoint import PyKMeansPoint

class PyKMeansCluster:
    position = []
    points = []
    clusterId = -1

    def __init__(self, position, clusterId):
        self.position = position
        self.clusterId = clusterId
        self.points = []

    def getPoints(self):
        return self.points

    def getId(self):
        return self.clusterId

    def getPosition(self):
        return self.position

    def setPosition(self):
        positionHasChange = False
        dimentions = []
        for point in self.points:
            dimIndex = 0
            for dim in point.getPosition():
                if dimIndex == len(dimentions):
                    dimentions.append(dim)
                else:
                    dimentions[dimIndex] += dim
                dimIndex += 1
        newPosition=[]
        for dim in dimentions:
            newPosition.append(dim / len(self.points))
        if self.positionHasChange(newPosition):
            positionHasChange = True
        self.position = newPosition
        return positionHasChange

    def isNot(self, otherCluster):
        retValue = True
        if self.getId() == otherCluster.getId():
            retValue = False
        return retValue

    def addPoint(self, point):
        self.points.append(point)

    def removePoint(self, pointToRemove):
        founded = False
        for point in self.points:
            if pointToRemove.getId() == point.getId():
                self.points.remove(point)
                founded = True
        if founded is False:
            raise Exception("Couldn't found given point to remove from Cluster.")

    def positionHasChange(self, newPosition):
        hasBeenChanged = False
        actualNumDims = len(self.position)
        newNumDims = len(newPosition)
        if actualNumDims == newNumDims:
            index = 0
            while index < actualNumDims:
                if abs(self.position[index] - newPosition[index]) > 0.0000000001:
                    hasBeenChanged = True
                index += 1

        else:
            raise Exception("Positions have not same dimentions")
        return hasBeenChanged
