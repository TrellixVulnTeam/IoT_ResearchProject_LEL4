dsS1Sensors = pd.read_csv(PATH + '/intermediate_datasets/S1Sensors_preprocessed.csv', engine = 'python')
# ds.head(n=1)
# ds.info()

subActNumKeyWithStringDict = pd.Series(dsS1Sensors.concat.values, 
                                       dsS1Sensors.subActNum.values).to_dict()

subActNumKeyWithStringDictNoDupes = {}

for key,value in subActNumKeyWithStringDict.items():
    if value not in subActNumKeyWithStringDictNoDupes.values():
        subActNumKeyWithStringDictNoDupes[key] = value
        
ds['subAct'] = ds['subActNum'].map(subActNumKeyWithStringDict)

# ds.head(n=2)

seen = {}
dupes = []

for x in ds.subActNum:
    if x not in seen:
        seen[x] = 1
    else:
        if seen[x] == 1:
            dupes.append(x)
        seen[x] += 1
        


#%run -i add_DAY_WDWE_phaseII.py