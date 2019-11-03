a = dsS1Sensors.iloc[:,3]
specialChar = '/'
reqEnergy = 'ligh|burn|mach|toas|freez|dvd|lamp|washer|dry|exh|disp|frig|oven|hot|micro'
b = a.str.contains(reqEnergy, regex = True)
c = a.str.contains(specialChar, regex = True)
dsS1Sensors['reqEnergy'] = b
dsS1Sensors['specialChar'] = c
forwardSlashFilter = dsS1Sensors['concat'].str.contains('/|\|', regex = True) # Find characters `/`, `\`