# SubAct Number KEY with String DICTIONARY JSON 
PATH = '/Users/alistairgj/Documents/GitHub/IoT_ResearchProject'
subActNumKeyWithStringDict = pd.Series(dsS1Sensors.concat.values, 
                                       dsS1Sensors.subActNumConcat.values).to_dict()
subActNumKeyWithStringJson = json.dumps(subActNumKeyWithStringDict)
f = open(PATH + '/JSON/subActNumKeyWithStringDict.json','w')
f.write(subActNumKeyWithStringJson)
f.close()

# SubAct Number KEY with Boolean Energy DICTIONARY JSON 
subActNumKeyWithEnergyDict = pd.Series(dsS1Sensors.reqEnergy.values, 
                                    dsS1Sensors.subActNumConcat.values).to_dict()
subActNumKeyWithEnergyJson = json.dumps(subActNumKeyWithEnergyDict)
f = open(PATH + '/JSON/subActNumKeyWithEnergyDict.json', 'w')
f.write(subActNumKeyWithEnergyJson)
f.close()

# SubAct String KEY with Boolean Energy DICTIONARY JSON 
subActKeyWithEnergyDict = pd.Series(dsS1Sensors.reqEnergy.values, 
                                    dsS1Sensors.concat.values).to_dict()
subActKeyWithEnergyJson = json.dumps(subActKeyWithEnergyDict)
f = open(PATH + '/JSON/subActKeyWithEnergyDict.json','w')
f.write(subActKeyWithEnergyJson)
f.close()


#Image(filename = PATH + '/images/subActNumKeyWithEnergyDict.jpg')
#print("subActNum_100: ", subActNumKeyWithEnergyDict['subActNum_100'])    # Checking the dictionary
#print("subActNum_101: ", subActNumKeyWithEnergyDict['subActNum_101']) 
# Image(filename = PATH + '/images/subActNumKeyWithStringDict.jpg')

#Use the new datastore datastructure
#print datastore["office"]["parking"]["style"]
# https://realpython.com/python-json/

#print("subActNum_100: ", subActNumKeyWithStringDict['subActNum_100'])    # Checking the dictionary
#print("subActNum_101: ", subActNumKeyWithStringDict['subActNum_101']) 

# Image(filename = PATH + '/images/subActKeyWithEnergyDict.jpg')

#print("bathroom_door:       ", subActKeyWithEnergyDict['bathroom_door'])    # Checking the dictionary
#print("bathroom_exhaustfan: ", subActKeyWithEnergyDict['bathroom_exhaustfan']) 
