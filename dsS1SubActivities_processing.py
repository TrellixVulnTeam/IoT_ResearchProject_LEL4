from datetime import datetime

step1 = np.array(dsS1)
step2 = step1.flatten()
step3 = list(chunked(step2, 5))

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

numericConcat = []
numericSep = []
actConcat = []
actSep = []
startConcat = []
startSep = []
endConcat = []
endSep = []

i = 0
while i < len(step3):
    numericConcat.append(step3[i][1])
    numericSep.append([x.strip() for x in numericConcat[i].split(',')])
    actConcat.append(step3[i][2])
    actSep.append([x.strip() for x in actConcat[i].split(',')])
    startConcat.append(step3[i][3])
    startSep.append([x.strip() for x in startConcat[i].split(',')])
    endConcat.append(step3[i][4])
    endSep.append([x.strip() for x in endConcat[i].split(',')])
    i = i + 1    
    
dateStringList = []

i = 0
while i < len(step3):
    for x in range(len(numericSep[i])):
        dateStringList.append(dateList[i])
    i = i + 1
    
flat_numericSep = []                # Constructing an array 
for sublist in numericSep:
    for item in sublist:
        flat_numericSep.append(item)

flat_actSep = []
for sublist in actSep:
    for item in sublist:
        flat_actSep.append(item)

flat_startSep = []
for sublist in startSep:
    for item in sublist:
        flat_startSep.append(item)

flat_endSep = []
for sublist in endSep:
    for item in sublist:
        flat_endSep.append(item)

zippedList = list(zip(flat_numericSep, flat_actSep, dateStringList, flat_startSep, flat_endSep))
ds = pd.DataFrame(zippedList, columns = ['subActNum', 'subAct', 'date', 'startTime', 'endTime'])
        

start = (ds.date + " " + ds.startTime)
end = (ds.date + " " + ds.endTime)

startList = []
endList = []

i = 0
while i < len(start):
    startList.append(datetime.strptime(start[i], '%m/%d/%Y %H:%M:%S'))
    endList.append(datetime.strptime(end[i], '%m/%d/%Y %H:%M:%S'))
    i = i + 1
    
zippedList = list(zip(flat_numericSep, flat_actSep, startList, endList))
ds = pd.DataFrame(zippedList, columns = ['subActNum', 'subAct', 'start', 'end'])
ds = ds.sort_values('start')
ds.reset_index(drop = True, inplace = True)