from datetime import datetime

# Convert to an array structure using numpy
step1 = np.array(dsS1)
# The 2D array was flattened to a 1D array
step2 = step1.flatten()
# Chunking into groups of 5
step3 = list(chunked(step2, 5))

# Creating temporary data structures
tempStringList = []
tempStripList = []
activityList = []
dateList = []
tempStartTimeList = []
tempEndTimeList = []

# Populating the temporary data structures with individual items of data
i = 0
while i < len(step3):
    tempStringList.append(step3[i][0])
    tempStripList.append([x.strip() for x in tempStringList[i].split(',')])
    activityList.append(tempStripList[i][0])
    dateList.append(tempStripList[i][1])
    tempStartTimeList.append(tempStripList[i][2])
    tempEndTimeList.append(tempStripList[i][3])
    i = i + 1
    
zippedList = list(zip(activityList, dateList, tempStartTimeList, tempEndTimeList))
ds = pd.DataFrame(zippedList, columns = ['activity', 'date', 'startTime', 'endTime'])
dsIntermediate = pd.DataFrame(zippedList, columns = ['activity', 'date', 'startTime', 'endTime'])
dsIntermediate.to_csv(PATH + '/intermediate_datasets/S1Activities_intermediate.csv', index = False)
start = (ds.date + " " + ds.startTime)
end = (ds.date + " " + ds.endTime)

startList = []
endList = []

i = 0
while i < len(start):
    startList.append(datetime.strptime(start[i], '%m/%d/%Y %H:%M:%S'))
    endList.append(datetime.strptime(end[i], '%m/%d/%Y %H:%M:%S'))
    i = i + 1
    
zippedList = list(zip(activityList, startList, endList))
ds = pd.DataFrame(zippedList, columns = ['activity', 'start', 'end'])
ds.to_csv(PATH + '/intermediate_datasets/S1Activities_ds.csv', index = False)
# INFO!!!!






