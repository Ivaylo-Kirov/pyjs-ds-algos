import math

coll = [1, 3, 4, 6, 7, 8, 11, 12, 13, 15, 23, 25, 34]

def binarySearch(coll, value):
    mid = math.floor(len(coll) / 2)

    start = 0
    end = len(coll) - 1

    while start < end:
        mid = math.floor((end + start) / 2)
        if value == coll[start] or value == coll[end] or value == coll[mid]:
            return True
        if value > coll[mid]:
            start = mid + 1
        else:
            end = mid
    return False

result = binarySearch(coll, 13)
print(result)