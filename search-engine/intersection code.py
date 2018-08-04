#written according the psudo code intersection code in class presentation 
def intersection(dic1_indexes, dic2_indexes):
    p1, p2 = 0, 0
    inter_indexes = []

    while p1 < len(dic1_indexes) and p2 < len(dic2_indexes):
        if dic1_indexes[p1] < dic2_indexes[p2]:
            p1 += 1
        elif dic1_indexes[p1] > dic2_indexes[p2]:
            p2 += 1
        else:
            inter_indexes.append(dic1_indexes[p1])
            p1 += 1
            p2 += 1

    return inter_indexes


# just for example i made those dictionary

dict1 = {'Mickey': [1, 2, 4, 6, 8, 9, 11, 17]}
dict2 = {'Minnie': [1, 3, 6, 11, 17]}

# the get function in dictionary allows me to get the values in my dictionary as a list
inter_list = intersection(dict1.get('Mickey'), dict2.get('Minnie'))
print(inter_list)
