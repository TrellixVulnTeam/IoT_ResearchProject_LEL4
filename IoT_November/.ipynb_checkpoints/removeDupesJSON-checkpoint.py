subActStringWithNumDictNoDupes = dict([(value, key) for key,
                                       value in subActNumKeyWithStringDictNoDupes.items()])
ds['subActNum'] = ds['subAct'].map(subActStringWithNumDictNoDupes)