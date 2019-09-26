ds = pd.read_csv(PATH + '/intermediate_datasets/S1SubActivities_timeStampRanges.csv', index_col = None)
ds = ds.drop(columns = ['durationSec', 'dayNumeric', 'DAY', 'WDWE', 'HOUR'])

ds.start = pd.to_datetime(ds.start, format = '%Y-%m-%d %H:%M:%S')
ds.end = pd.to_datetime(ds.end, format = '%Y-%m-%d %H:%M:%S')

start = ds.start
end = ds.end

tempTimeStamp = []
i = 0
while i < len(ds):
    tempTimeStamp.append(pd.date_range(start = start[i], end = end[i], freq = 's'))
    i += 1

tempNumTimeStamps = []
i = 0
while i < len(ds):
    tempNumTimeStamps.append(len(tempTimeStamp[i]))
    i += 1
    
ds['actDuration'] = tempNumTimeStamps
ds['timeStampList'] = tempTimeStamp

timeStampVector = ds['timeStampList']

#timeStampVector[1]

DTArrayList = []
i = 0
while i < len(ds):
    DTArrayList.append(pd.DatetimeIndex.to_pydatetime(timeStampVector[i]))
    i = i + 1
    
ds['timeStampArrayList'] = DTArrayList