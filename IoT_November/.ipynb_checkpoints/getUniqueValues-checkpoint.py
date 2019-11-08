def getUniqueValues(list1):  # Function to get unique values
    unique_list = []  # Intilize a null list

    for x in list1:  # Traverse for all elements
        if x not in unique_list:  # Check if exists in unique_list or not
            unique_list.append(x)  # Append to unique_list
    return unique_list


#    for x in unique_list:                    # Print list
#        print(x)
