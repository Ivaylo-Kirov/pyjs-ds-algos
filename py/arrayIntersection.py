
def arrayIntersection(nums1, nums2):
    result = []
    uniques = set()
    for num in nums1:
        uniques.add(num)
    
    for num in nums2:
        if num in uniques and num not in result:
            result.append(num)

    return result


print(arrayIntersection([4,9,5], [9,4,9,8,4]))
print('hi')

#Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
#Output: [9,4]
#Intersection means common elements
# I need to return unique list (set)