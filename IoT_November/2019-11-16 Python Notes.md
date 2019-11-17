ds.to_csv(PATH + '/intermediate_datasets/S1SubActivities_temporalFeaturesCLEANSED.csv', index = False)



Initial and processed data box plot (A) and heat maps (B = day of week versus duration in seconds mapped by count, C = day of week versus hour of day mapped by count) for the bathroom toiletflush sub activity.


```{r}
df_METRIC <- read_csv("/Users/alistairgj/Documents/GitHub/IoT_ResearchProject/IoT_November/intermediate_datasets/df_METRIC.csv")
df_ACC <- read_csv("/Users/alistairgj/Documents/GitHub/IoT_ResearchProject/IoT_November/intermediate_datasets/df_ACC.csv")
```


```r TAB_fridge, echo=FALSE, results='asis'
fridge <- read_csv('/Users/alistairgj/Documents/GitHub/IoT_ResearchProject/IoT_November/intermediate_datasets/S1SubActivities_fridge.csv')
head(fridge, n=5) %>% kable(format = "latex", caption = "Example of duplicate sub-activity number removal", booktabs = T) %>% 
  kable_styling(latex_options = c("hold_position", "striped", "scale_down"),
                bootstrap_options = c("striped", "hover", "condensed"),
                font_size = 8) %>% add_header_above(c("Prior to duplicate removal" = 4, "Post to duplicate removal" = 4))
```

```r TAB_dsSUBActFinal, echo=FALSE, results='asis'}
df <- read_csv('/Users/alistairgj/Documents/GitHub/IoT_ResearchProject/IoT_November/intermediate_datasets/S1SubActivities_ds.csv')
head(df) %>% kable(format = "latex", caption = "The S1 sub-activities tidy dataset", booktabs = T) %>% 
  kable_styling(latex_options = c("hold_position", "striped"),
                bootstrap_options = c("striped", "hover", "condensed"),
                font_size = 8)
```




`s = ds.apply(lambda x: pd.Series(x['timeStampArrayList']),axis=1).stack().reset_index(level=1, drop=True)`

```python
import time
from binge import B

import random
import pandas as pd
import numpy as np
from multiprocessing import Pool

def parallelize_dataframe(df, func, n_cores=4):
    df_split = np.array_split(df, n_cores)
    pool = Pool(n_cores)
    df = pd.concat(pool.map(func, df_split))
    pool.close()
    pool.join()
    return df

parallelize_dataframe(ds, ds.apply(lambda x: pd.Series(x['timeStampArrayList']),axis=1).stack().reset_index(level=1, drop=True), n_cores=4)


s0 = segmentDF[0].apply(lambda x: pd.Series(x['timeStampArrayList']),axis=1).stack().reset_index(level=1, drop=True)
s1 = segmentDF[1].apply(lambda x: pd.Series(x['timeStampArrayList']),axis=1).stack().reset_index(level=1, drop=True)
s2 = segmentDF[2].apply(lambda x: pd.Series(x['timeStampArrayList']),axis=1).stack().reset_index(level=1, drop=True)
s3 = segmentDF[3].apply(lambda x: pd.Series(x['timeStampArrayList']),axis=1).stack().reset_index(level=1, drop=True)
s4 = segmentDF[4].apply(lambda x: pd.Series(x['timeStampArrayList']),axis=1).stack().reset_index(level=1, drop=True)
s5 = segmentDF[5].apply(lambda x: pd.Series(x['timeStampArrayList']),axis=1).stack().reset_index(level=1, drop=True)
s6 = segmentDF[6].apply(lambda x: pd.Series(x['timeStampArrayList']),axis=1).stack().reset_index(level=1, drop=True)
s7 = segmentDF[7].apply(lambda x: pd.Series(x['timeStampArrayList']),axis=1).stack().reset_index(level=1, drop=True)


segmentDF[0] = segmentDF[0].drop('end', axis=1).join(s0) 
segmentDF[0] = segmentDF[0].drop(columns = ['timeStampArrayList'])
segmentDF[0] = segmentDF[0].set_index('duration')
segmentDF[0]['subActNum'] = segmentDF[0]['subActNum'].astype(str)
segmentDF[0] = segmentDF[0].drop(columns = ['actDuration'])

segmentDF[7].to_csv(PATH + '/intermediate_datasets/segment7.csv',index = True)

ds = pd.concat([segmentDF[0], segmentDF[1], segmentDF[2], segmentDF[3], segmentDF[4], segmentDF[5], segmentDF[6], segmentDF[7]], ignore_index=False)