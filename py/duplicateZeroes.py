
def duplicateZeroes(arr):
    i = 0

    initLen = len(arr) - 1

    while i <= initLen:
        if arr[i] == 0:
            arr = arr[:i+1] + [0] + arr[i+1:initLen + 1]
            i += 1
            initLen += 1
        i += 1
    # there is a bug here as length remains the same after a new zero is added, so the last few items get deleted
    # idea is to set initial length as a variable, and then increase it manually az zeroes are added


duplicateZeroes([1,0,2,3,0,4,5,0])