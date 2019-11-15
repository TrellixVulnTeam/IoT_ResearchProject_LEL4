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

# Creating temporary data structures
1numericConcat = []
2numericSep = []
3actConcat = []
4actSep = []
5startConcat = []
6startSep = []
7endConcat = []
8endSep = []

# Populating the temporary data structures with individual items of data
i = 0
while i < len(step3):
    1numericConcat.append(step3[i][1])
    2numericSep.append([x.strip() for x in 1numericConcat[i].split(',')])
    3actConcat.append(step3[i][2])
    4actSep.append([x.strip() for x in 3actConcat[i].split(',')])
    5startConcat.append(step3[i][3])
    6startSep.append([x.strip() for x in 5startConcat[i].split(',')])
    7endConcat.append(step3[i][4])
    8endSep.append([x.strip() for x in 7endConcat[i].split(',')])
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

#len(flat_numericSep), len(flat_actSep), len(flat_startSep), len(flat_endSep)
        
zippedList = list(zip(flat_numericSep, flat_actSep, dateStringList, flat_startSep, flat_endSep))
ds = pd.DataFrame(zippedList, columns = ['subActNum', 'subAct', 'date', 'startTime', 'endTime'])
dsIntermediate = pd.DataFrame(zippedList, columns = ['subActNum', 'subAct', 'date', 'startTime', 'endTime'])
dsIntermediate.to_csv(PATH + '/intermediate_datasets/S1SubActivities_intermediate.csv', index = False)        

start = (ds.date + " " + ds.startTime)
end = (ds.date + " " + ds.endTime)

# Creating temporary data structures
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

# Replacing the special character values
ds['subAct'].replace('Office/study', 'Study', inplace=True)

ds.to_csv(PATH + '/intermediate_datasets/S1SubActivities_ds.csv', index = False)

# Converting subActNum to numeric
ds['subActNum'] = pd.to_numeric(ds.subActNum)

# INFO!!!!