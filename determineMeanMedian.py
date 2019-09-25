subActNames = ['bathroom_cabinet', 'bathroom_medicinecabinet', 'study_drawer', 
                'bedroom_drawer', 'kitchen_cabinet', 'kitchen_microwave', 
                'kitchen_door', 'bathroom_showerfaucet', 'kitchen_drawer', 
                'bathroom_sinkfaucet-hot', 'kitchen_freezer', 'bathroom_door',
                'kitchen_toaster', 'kitchen_lightswitch', 'study_lightwitch', 
                'kitchen_dishwasher', 'livingroom_lightswitch']

subActRows = []

for subActName in subActNames:
    dsNew = ds[ds.subAct == subActName]
    dsNew = ds[ds.subAct == subActName]
    count = dsNew.durationSec.count()
    median = dsNew.durationSec.median()
    mean = dsNew.durationSec.mean() 
    std = dsNew.durationSec.std()
    #outliers = detect_outlier(dsNew['durationSec'])
    
    column = {'SubAct': subActName,'Count': count,'Median': median, 'Mean': mean, 'Std': std}
    subActRows.append(column)

allMedianValues = pd.DataFrame(subActRows, index=None, 
                            columns=['SubAct', 'Count', 'Median', 'Mean', 'Std'])

