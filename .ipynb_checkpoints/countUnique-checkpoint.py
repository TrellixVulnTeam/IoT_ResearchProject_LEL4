# Unique subActNum list
unique_list = []
for x in ds.subActNum:                  # Traverse for all elements 
    if x not in unique_list:            # Check if exists in unique_list or not 
        unique_list.append(x)   
print(len(unique_list))