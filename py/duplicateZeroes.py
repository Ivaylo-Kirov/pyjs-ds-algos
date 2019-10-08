
def duplicateZeroes(arr):
    i = 0

    while i < len(arr) - 1:
        if arr[i] == 0:
            arr = arr[:i+1] + [0] + arr[i+1:len(arr) - 1]
            i += 1
        i += 1


duplicateZeroes([1,0,2,3,0,4,5,0])