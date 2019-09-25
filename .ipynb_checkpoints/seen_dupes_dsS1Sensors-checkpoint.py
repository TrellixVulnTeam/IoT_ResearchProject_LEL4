seen = {}
dupes = []

for x in dsS1Sensors.concat:
    if x not in seen:
        seen[x] = 1
    else:
        if seen[x] == 1:
            dupes.append(x)
        seen[x] += 1
        
for i in seen:                  # Adding value counts for dupes
    if (seen[i] > 1 and seen[i] <= 9):
        print(seen[i], " ", i)
    if (seen[i] >= 10):
        print(seen[i], "", i)