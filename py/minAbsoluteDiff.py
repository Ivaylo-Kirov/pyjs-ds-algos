def minimumAbsDifference(arr):
        # sort
        arr.sort()
        # iterate and maintain min
        # if min is 1, break
        minDiff = 20000000
        for i in range(len(arr)-1):
            if abs(arr[i] - arr[i+1]) < minDiff:
                minDiff = abs(arr[i] - arr[i+1])
        
        # 
        # now find all pairs and sort them
        valueHash = set(arr)
        resultPairs = []
        # all values in a hash
        # iterate and search for +minDiff of current
        for i in range(len(arr)-1):
            if arr[i]+minDiff in valueHash:
                # if it matches, add it to results
                resultPairs.append([arr[i], arr[i]+minDiff])
        
        # still need i - 1s
        return resultPairs
        
        

result = minimumAbsDifference([1,3,6,10,15])
print('hi')

# Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements. 

# Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

# a, b are from arr
# a < b
# b - a equals to the minimum absolute difference of any two elements in arr
 

# Example 1:

# Input: arr = [4,2,1,3]
# Output: [[1,2],[2,3],[3,4]]
# Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.
# Example 2:

# Input: arr = [1,3,6,10,15]
# Output: [[1,3]]
# Example 3:

# Input: arr = [3,8,-10,23,19,-4,-14,27]
# Output: [[-14,-10],[19,23],[23,27]]