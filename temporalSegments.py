charts = []
for subActNum in unique_list:
    dsCheck = ds[ds['subActNum'] == subActNum]
    
    color = alt.condition(alt.datum.day > 4,
                      alt.value('orange'),
                      alt.value('grey'))
    
    df = pd.DataFrame({ 
        'start': dsCheck.start, 
        'end': dsCheck.end,
        'day': dsCheck.dayNumeric})
    
    subAct = ds[ds.subActNum == subActNum].subAct.head(1).item()     # Correct 'item' error

    chart = alt.Chart(df.reset_index(), title = "Sub-activity: " + subAct +
                      " // " + "Sub-activity number: " + str(subActNum)).mark_bar().encode(
        y = 'date(start):O',
        x = 'hoursminutes(start)',
        x2 = 'hoursminutes(end)',
        color = color,
        detail = 'index').properties(width=750).interactive()
    
    charts.append(chart)
    
    
boxPlots = []
for subActNum in unique_list:
    dsCheck = ds[ds['subActNum'] == subActNum]
    
    color = alt.condition(alt.datum.day > 4,
                      alt.value('orange'),
                      alt.value('grey'))
    
    df = pd.DataFrame({ 
        'durationSec': dsCheck.durationSec,
        'subAct' : dsCheck.subAct,
        'day': dsCheck.dayNumeric,
        'WDWE': dsCheck.WDWE})
    
    subAct = ds[ds.subActNum == subActNum].subAct.head(1).item()     # Correct 'item' error

    chart = alt.Chart(df, title = "Sub-activity: " + subAct +
                      " // " + "Sub-activity number: " + str(subActNum)).mark_boxplot().encode(
        x = 'durationSec',
        y = 'subAct',
        row = 'WDWE',
        fill = 'WDWE:N').properties(width=550).interactive()
    
    boxPlots.append(chart)   
    
df = pd.DataFrame({ 
         'fill': ['orange', 'grey']})

alt.Chart(ds67).mark_boxplot().encode(
    x = 'durationSec',
    y = 'subAct',
    row = 'WDWE',
    fill = 'WDWE:N'
).properties(width = 550, height = 30).interactive()