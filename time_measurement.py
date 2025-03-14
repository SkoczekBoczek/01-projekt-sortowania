import time

def TimeMeasure(sortFunction, data):
    dataCopy = data[:]
    startTime = time.time()
    sortFunction(dataCopy)
    endTime = time.time()
    timeRes = round((endTime - startTime), 10)
    return timeRes