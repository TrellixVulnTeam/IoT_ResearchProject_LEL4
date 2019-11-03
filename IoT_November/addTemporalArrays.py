import time
from datetime import datetime

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