import time
from datetime import datetime

# Capture the original DS
ds_initial = ds.copy()

start = ds.start
end = ds.end

tempTimeStamp = []
i = 0
while i < len(ds):
    tempTimeStamp.append(pd.date_range(start=start[i], end=end[i], freq='s'))
    i += 1

tempNumTimeStamps = []
i = 0
while i < len(ds):
    tempNumTimeStamps.append(len(tempTimeStamp[i]))
    i += 1

ds['actDuration'] = tempNumTimeStamps
ds['timeStampList'] = tempTimeStamp

timeStampVector = ds['timeStampList']

DTArrayList = []
i = 0
while i < len(ds):
    DTArrayList.append(pd.DatetimeIndex.to_pydatetime(timeStampVector[i]))
    i = i + 1

ds['timeStampArrayList'] = DTArrayList

ds = ds.drop(columns = ['durationSec', 'timeStampList'])
             
ds.to_csv('intermediate_datasets/S1SubActivities_timeStampRanges.csv',index = False)
             
# Capturing the first intermediate DS
ds_int_one = ds.copy()
  
             
ds = ds.set_index(start, drop = True)
ds = ds.drop(columns = ['subAct','dayNumeric', 'DAY', 
                        'WDWE', 'HOUR', 'start'])

# Capturing the second intermediate DS             
ds_int_two = ds.copy()             
#
             
s = ds.apply(lambda x: pd.Series(x['timeStampArrayList']),axis=1).stack().reset_index(level=1, drop=True)
s.name = 'duration'
ds = ds.drop('end', axis=1).join(s)             

# Capturing the second intermediate DS             
ds_int_three = ds.copy()             
# IDX = start
# COLS = 'subActNum', 'actDuration', 'timeStampArrayList', 'duration'

ds = ds.drop(columns = ['timeStampArrayList'])

ds = ds.set_index('duration')
             
ds.to_csv(PATH + '/intermediate_datasets/S1SubActivities_timeRangeMelt.csv', index=False)

ds_int_four = ds.copy()
             
ds['subActNum'] = ds['subActNum'].astype(str)

ds = ds.drop(columns = ['actDuration'])

ds = pd.get_dummies(ds)

ds_final = ds.copy()

ds.to_csv(PATH + '/intermediate_datasets/S1SubAct_B.csv', index='duration')

