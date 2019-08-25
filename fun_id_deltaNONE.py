import datetime as dt

def id_delta(events, n=1, delta_threshold=dt.timedelta(-99)):
    nns = []
    for row in events.itertuples():
        #print(row)
        start_time = getattr(row, 'start')
        end_time = getattr(row, 'end')
        subActNum = getattr(row, 'subActNum')
        row_index = getattr(row, 'Index')
        
        nn = events[(events.start >= start_time) & 
                    (events.index != row_index) & 
                    ((start_time - events.start) > delta_threshold)][:n]
        #print(len(nn))
        ordered = pd.DataFrame()
        ordered['Dummy'] = nn['subActNum']
        ordered['EventA'] = subActNum
        ordered['EventB'] = nn['subActNum']
        ordered['EvA_Start'] = start_time
        ordered['EvA_End'] = end_time
        ordered['EvB_Start'] = nn['start']
        ordered['EvB_End'] = nn['end']
        del ordered['Dummy']
        nns.append(ordered)
  
    #print(nns)
    result = pd.concat(nns)

    result['Delta'] = np.where(result['EvA_Start']==result['EvB_Start'], 
                               None, 
                               (result['EvA_End'] - result['EvB_Start']) / 1000000000)
    return result