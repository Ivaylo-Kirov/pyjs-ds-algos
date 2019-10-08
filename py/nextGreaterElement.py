def nextGreaterElement(nums1, nums2):
    result = []
    for num in nums1:
        foundIndex = nums2.index(num)
        found = False
        for i in range(foundIndex + 1, len(nums2)):
            if nums2[i] > num:
                result.append(nums2[i])
                found = True
                break
        if not found:
            result.append(-1)


    return result

result = nextGreaterElement([4,1,2], [1,3,4,2])