import pandas as pd 
d = {'Type': ['An array of comma-sep strings', 
             'An array of comma-sep strings',
             'An array of comma-sep strings',
             'An array of comma-sep strings',
             'An array of comma-sep strings'], 
     'Description ': ['Activity information, date, start time, end time',
                      'Sub-activity reference value',
                      'Sub-activity descriptive value',
                      'Sub-activity start time',
                      'Sub-activity end time'],
    'Desired Type' : ['...',
                      'Levels',
                      'Levels',
                      'Datetime including the date extracted from the index 3 rows above',
                      'Datetime including the date extracted from the index 4 rows above']}
df = pd.DataFrame(data=d)
