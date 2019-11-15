seen = {}
dupes = []
dsFridge = ds[ds['subAct'].str.contains("kitchen_refrigerator")] 
for x in dsFridge.subActNum:
    if x not in seen:
        seen[x] = 1
    else:
        if seen[x] == 1:
            dupes.append(x)
        seen[x] += 1
print(dupes)