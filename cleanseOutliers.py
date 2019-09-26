for row in allMedianValues.iterrows():
    ds.loc[(ds['subAct'] == row[1].SubAct) &
           (ds['durationSec'] > row[1].Median + 0.5 * row[1].Std),
           'durationSec'] = round(row[1].Median)

from datetime import datetime, timedelta
ds.end = ds.apply(lambda x: x.start + timedelta(seconds=x.durationSec), axis=1)
ds['durationSec'] += 1