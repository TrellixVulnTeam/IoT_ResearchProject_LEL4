temp1 = dsS1Sensors[1] + '_' + dsS1Sensors[2]   # Creating a new vector of concatenated column 1 & 2
temp2 = temp1.str.replace(" ", "")              # Removing whitespace between strings
temp3 = temp2.str.lower()                       # Changing all text to lowercase
temp4 = temp3.str.strip()                       # Striping any remaining whitespace
dsS1Sensors[3] = temp4                          # Adding the precessed vector back into the dataset
dsS1Sensors.rename(columns={0:'subActNum', 
                            1:'room',
                            2:'activity',
                            3:'concat',
                            4:'energyReq'}, 
                   inplace=True)