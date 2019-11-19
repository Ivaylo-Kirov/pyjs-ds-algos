# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

# Note:

# The number of elements initialized in nums1 and nums2 are m and n respectively.
# You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
# Example:

# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3

# Output: [1,2,2,3,5,6]

def merge(nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """

    # maintain 1 and 2 indecies
    nums1i = 0
    nums2i = 0
    initialM = m

    while nums1i < m and nums2i < n:
        while nums1i < m and nums1[nums1i] <= nums2[nums2i]:
            nums1i += 1
        # now we found a bigger value in nums2, so insert it in the correct index
        nums1.insert(nums1i, nums2[nums2i])
        del nums1[-1]
        m += 1
        nums1i += 1
        nums2i += 1

    # iterate and compare to see how to adjust indecies
    # increment required indecies based on results

    # stragglers
    # if stragglers for nums1 exist, they are already in their correct place
    
    while nums2i < n:
        nums1.insert(initialM + nums2i, nums2[nums2i])
        del nums1[-1]
        nums2i += 1


merge([1,2,3,0,0,0], 3, [2,5,6], 3)
print('hi')