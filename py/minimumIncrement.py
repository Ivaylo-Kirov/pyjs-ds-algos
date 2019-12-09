# Given an array of integers A, a move consists of choosing any A[i], and incrementing it by 1.

# Return the least number of moves to make every value in A unique.

# Example 1:

# Input: [1,2,2]
# Output: 1
# Explanation:  After 1 move, the array could be [1, 2, 3].
# Example 2:

# Input: [3,2,1,2,1,7]
# Output: 6
# Explanation:  After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
# It can be shown with 5 or less moves that it is impossible for the array to have all unique values.

def minIncrementForUnique(A):
    result = 0
    count_d = dict()

    for num in A:
        if num in count_d:
            count_d[num] += 1
        else:
            count_d[num] = 1
    
    #A.sort() # instead of sorting, just check if it's in DICT and if its count is > 1
    for num in A:
        if count_d[num] > 1: # there is a duplicate, so deal with it
            keep_going = True
            target = num
            while keep_going:
                # this must increment until it sees a num that's not in DICT, and then +=1 that in the DICT
                result += 1
                target += 1
                if target not in count_d:
                    count_d[target] = 1
                    keep_going = False
            count_d[num] -= 1

    return result


result = minIncrementForUnique([3,2,1,2,1,7])
print('hi')