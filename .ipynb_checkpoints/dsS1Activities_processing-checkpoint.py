from datetime import datetime

step1 = np.array(dsS1)
step2 = step1.flatten()
step3 = list(chunked(step2, 5))

#dimLength = []
#i = 0
#while i < len(a):
#    dimLength.append(len(a[i]))
#    i = i + 1

tempStringList = []
tempStripList = []
activityList = []
dateList = []
tempStartTimeList = []
tempEndTimeList = []

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