dsS1Sensors['concat'].replace('office/study_drawer','study_drawer',inplace=True)
dsS1Sensors['room'].replace('Office/study','Study',inplace=True)
dsS1Sensors['concat'].replace('office/study_lightswitch','study_lightwitch',inplace=True)
dsS1Sensors['subActNumConcat'] = 'subActNum_' + dsS1Sensors['subActNum'].astype(str)
dsS1Sensors.drop(columns=['specialChar'], inplace=True)