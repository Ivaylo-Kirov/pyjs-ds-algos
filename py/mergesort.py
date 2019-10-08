# logic works, but issue with how to return and what to return
# seems related to 'pass by reference'.. if this was c++ I could overwrite coll with aux at the end

import math
#coll = [1, 12, 13, 5, 3, 4, 23, 25, 6, 7, 8, 11, 15, 34]
coll = [1, 12, 8]
#currently fails because each 'half' is not already sorted, so I can't merge them

def mergeSort(coll, start, end):
    if start < end:
        mid = math.floor((end + start) / 2)
        mergeSort(coll, start, mid)
        mergeSort(coll, mid + 1, end)
        merge(coll[start:mid+1], coll[mid+1:end+1])

def merge(coll1, coll2):
    aux = []
    coll1i = 0
    coll2i = 0

    while coll1i < len(coll1) and coll2i < len(coll2):
        if coll1[coll1i] < coll2[coll2i]:
            aux.append(coll1[coll1i])
            coll1i += 1
        else:
            aux.append(coll2[coll2i])
            coll2i += 1
    
    #stragglers
    while coll1i < len(coll1):
        aux.append(coll1[coll1i])
        coll1i += 1
    while coll2i < len(coll2):
        aux.append(coll2[coll2i])
        coll2i += 1
    
mergeSort(coll, 0, len(coll) - 1)
print('hi')

