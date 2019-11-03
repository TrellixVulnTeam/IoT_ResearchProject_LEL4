unique_list = []  # Unique subActNum list
for x in ds.subActNum:  # Traverse for all elements
    if x not in unique_list:  # Check if exists in unique_list or not
        unique_list.append(x)

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

    subAct = ds[ds.subActNum == subActNum].subAct.head(1).item()  # Correct 'item' error

    chart = alt.Chart(df.reset_index(), title="Sub-activity: " + subAct +
                                              " // " + "Sub-activity number: " + str(subActNum)).mark_bar().encode(
        y='date(start):O',
        x='hoursminutes(start)',
        x2='hoursminutes(end)',
        color=color,
        detail='index').properties(width=680).interactive()

    charts.append(chart)