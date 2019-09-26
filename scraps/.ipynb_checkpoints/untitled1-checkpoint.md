https://altair-viz.github.io/user_guide/encoding.html

```{python}
ds.set_index(ds.start, inplace = True)
ds.insert((len(ds.columns)), "DAY", ds.index.dayofweek.astype(str), True)
ds.insert((len(ds.columns)), "WDWE", ds.index.dayofweek.astype(str), True)
```

```{python}
dayNumKeyWithDAYDict = pd.Series(['Mon','Tue','Wed','Thu','Fri','Sat','Sun'], ['0','1','2','3','4','5','6']).to_dict()
#dayNumKeyWithDAYDict
dayNumKeyWithWDWEDict = pd.Series(['WD','WD','WD','WD','WD','WE','WE'], ['0','1','2','3','4','5','6']).to_dict()
#dayNumKeyWithWDWEDict
```

ds = ds.replace({"DAY": dayNumKeyWithDAYDict})
ds = ds.replace({"WDWE": dayNumKeyWithWDWEDict})

# Pre-req = datetime is the index!
ds.reset_index(drop = True, inplace = True)


ds.to_csv('S1SubActivities_timeStampRanges.csv',index=False)

# DURATION
import datetime as dt
ds['deltaStartEnd'] = ds['end'] - ds['start']
ds['deltaStartEnd'] = ds['deltaStartEnd'].dt.total_seconds()

ds['HOUR'] = ds['start'].dt.hour

```{py}
ds.set_index(ds.start, inplace = True)                                      # Setting the start attribute as IDX
ds.insert((len(ds.columns)), "DAY", ds.index.dayofweek.astype(str), True)   # Adding the values for day of week (str?)

#ds.insert((len(ds.columns)), "WDWE", ds.index.dayofweek.astype(str), True) #
```

* Title with SubActNum and SubAct
* Start Date as Thu 03 March
* Weekends orange
* Weekdays blue
* 24till2
* 3till5
* 6till8
* 9till11
* 12till14
* 15till17
* 18till20
* 21till23


```{python}
#https://vega.github.io/vega-lite/tutorials/explore.html
#https://altair-viz.github.io/user_guide/customization.html
    
df = pd.DataFrame({ 
         'fill': ['orange', 'grey']})

alt.Chart(ds67).mark_boxplot().encode(
    x = 'durationSec',
    y = 'subAct',
    row = 'WDWE',
    fill = 'WDWE:N'
).properties(width = 550, height = 30).interactive()
```



ds = pd.read_csv('S1SubActivities_preprocessed.csv', index_col = None) 

Overwrite ALL
subAct ['bathroom_toiletflush'] DONE

Fill OUTLIER with Mean (excluding outliers)
subAct ['bathroom_cabinet', 'bathroom_medicinecabinet', 'study_drawer', 'bedroom_drawer',
        'kitchen_cabinet', 'kitchen_microwave', 'kitchen_door', 'bathroom_showerfaucet',
        'kitchen_drawer', 'bathroom_sinkfaucet', 'kitchen_freezer', 'bathroom_door',
        'kitchen_toaster']
        
DROP
subAct ['bedroom_jewelrybox', 'foyer_closet', 'kitchen_cereal', 'kitchen_containers', bedroom_lamp]