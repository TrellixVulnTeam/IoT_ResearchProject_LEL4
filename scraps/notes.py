

ds_new['Phase'] = "Afternoon"
ds_new.loc[ds_new['HOUR'] < 9, 'Phase'] = "Morning"
ds_new.loc[ds_new['HOUR'] >= 17, 'Phase'] = "Evening"
benchmark_usage = ds_new.groupby(['subAct','WDWE','Phase'])['durationSec'].mean()
benchmark_usage
### OUT:
#-------------------------------------------------
# subAct            WDWE  Phase    
# bathroom_cabinet  WD    Afternoon       6.862069
#                         Evening         2.833333
#                         Morning         4.800000
#                   WE    Afternoon       4.181818
#                         Evening         2.272727
#                                         ...     
# study_lightwitch  WD    Afternoon    1853.875000
#                         Evening      1427.285714
#                         Morning      1184.800000
#                   WE    Afternoon    1157.666667
#                         Evening      2532.000000
# Name: durationSec, Length: 164, dtype: float64
#-------------------------------------------------

benchmark_usage['bathroom_lightswitch']['WD']['Afternoon']
### OUT:
# 1726.4















