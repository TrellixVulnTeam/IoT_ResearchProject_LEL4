subActRows = []

for subActName in subActNames:
    dsNew = ds[ds.subAct == subActName]
    dsNew = ds[ds.subAct == subActName]
    count = dsNew.durationSec.count()
    median = dsNew.durationSec.median()
    mean = dsNew.durationSec.mean()
    std = dsNew.durationSec.std()
    # outliers = detect_outlier(dsNew['durationSec'])

    column = {'SubAct': subActName, 'Count': count, 'Median': median, 'Mean': mean, 'Std': std}
    subActRows.append(column)

allMedianValues = pd.DataFrame(subActRows, index=None,
                               columns=['SubAct', 'Count', 'Median', 'Mean', 'Std'])
allMedianValues.to_csv(PATH + '/intermediate_datasets/S1SubActivities_medianValues.csv', index = False) 