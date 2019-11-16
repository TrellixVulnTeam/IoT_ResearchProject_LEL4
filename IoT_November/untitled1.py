
segmentDF = np.array_split(ds, 8)

s0 = segmentDF[0].apply(lambda x: pd.Series(x['timeStampArrayList']),axis=1).stack().reset_index(level=1, drop=True)
s1 = segmentDF[1].apply(lambda x: pd.Series(x['timeStampArrayList']),axis=1).stack().reset_index(level=1, drop=True)
s2 = segmentDF[2].apply(lambda x: pd.Series(x['timeStampArrayList']),axis=1).stack().reset_index(level=1, drop=True)
s3 = segmentDF[3].apply(lambda x: pd.Series(x['timeStampArrayList']),axis=1).stack().reset_index(level=1, drop=True)
s4 = segmentDF[4].apply(lambda x: pd.Series(x['timeStampArrayList']),axis=1).stack().reset_index(level=1, drop=True)
s5 = segmentDF[5].apply(lambda x: pd.Series(x['timeStampArrayList']),axis=1).stack().reset_index(level=1, drop=True)
s6 = segmentDF[6].apply(lambda x: pd.Series(x['timeStampArrayList']),axis=1).stack().reset_index(level=1, drop=True)
s7 = segmentDF[7].apply(lambda x: pd.Series(x['timeStampArrayList']),axis=1).stack().reset_index(level=1, drop=True)

s0.name = 'duration'
s1.name = 'duration'
s2.name = 'duration'
s3.name = 'duration'
s4.name = 'duration'
s5.name = 'duration'
s6.name = 'duration'
s7.name = 'duration'







