import pandas as pd
import numpy as np
import time
from datetime import datetime
import pandas as pd

def add_DAY_WDWE_phaseI(ds):
    dayNumKeyWithDAYDict = pd.Series(['Mon','Tue','Wed','Thu','Fri','Sat','Sun'], ['0','1','2','3','4','5','6']).to_dict()
    dayNumKeyWithWDWEDict = pd.Series(['WD','WD','WD','WD','WD','WE','WE'], ['0','1','2','3','4','5','6']).to_dict()
    ds.set_index(ds.start, inplace = True)
    ds.insert((len(ds.columns)), "dayNumeric", ds.index.dayofweek.astype(str), True)
    ds.insert((len(ds.columns)), "DAY", ds.index.dayofweek.astype(str), True)
    ds.insert((len(ds.columns)), "WDWE", ds.index.dayofweek.astype(str), True)
    ds = ds.replace({"DAY": dayNumKeyWithDAYDict})
    ds = ds.replace({"WDWE": dayNumKeyWithWDWEDict})
    ds.reset_index(drop = True, inplace = True)
    ds['HOUR'] = ds['start'].dt.hour
    ds['durationSec'] = ds['end'] - ds['start']
    ds['durationSec'] = ds['durationSec'].dt.total_seconds()
    ds['durationSec'] = ds.durationSec.astype(int)
    return ds