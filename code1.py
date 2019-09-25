# %run -i code1.py
a = dsS1Sensors.iloc[:,3]
specialChar = '/'
reqElectricity = 'ligh|burn|mach|toas|freez|dvd|lamp|washer|dry|exh|disp|frig|oven|hot|micro'
b = a.str.contains(reqElectricity, regex = True)
c = a.str.contains(specialChar, regex = True)
dsS1Sensors['reqElectricity'] = b
dsS1Sensors['specialChar'] = c