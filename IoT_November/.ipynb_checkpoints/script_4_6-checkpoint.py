ds.index = pd.to_datetime(ds.index)
ds = ds.resample('min').max()

dsMin = ds.copy()

resampledLen = len(ds)
ds = ds.dropna(how = 'all')
resampledLenDropNA = len(ds)

dsHour = ds.resample('h').sum()
dsHour = dsHour.loc[:,].div(dsHour.sum(axis=1), axis=0)

resampledHourContainNA = dsHour.isnull().values.any()

dsHour = dsHour.dropna()

dsHourFreqMelt = dsHour.stack().reset_index()
dsHourFreqMelt.columns = ['timeStamp', 'subAct', 'freq']

dsHourFreqMeltLength = len(dsHourFreqMelt)

dsHourFreqMelt = dsHourFreqMelt[dsHourFreqMelt.freq != 0]

dsHourFreqMeltLengthDROP_ZERO = len(dsHourFreqMelt)
