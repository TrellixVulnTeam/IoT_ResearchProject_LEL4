from datetime import datetime, timedelta
ds['durationSec'] = np.where(ds['subActNum'] == 100, 1, ds['durationSec'])
ds['end'] = np.where(ds['subActNum'] == 100, 
                     ds['start'] + timedelta(seconds=1), ds['end'])