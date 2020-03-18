class Queues:
    def __init__(self):
        self.__data = []

    def getQueue(self):
        return self.__data

    def enterData(self, newData):
        return self.__data.append(newData)

    def remove(self):
        return self.__data.pop(0)

    def emptyQueue(self):
        pos = 0
        for i in range(0, pos + 1):
            return self.__data.pop(0)

    def lenQueue(self):
        return len(self.__data)
