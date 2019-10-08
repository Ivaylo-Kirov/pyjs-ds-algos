
def findPeak(nums):
    peak = 0
    peakIndex = 0
    for i in range(len(nums)):
        if nums[i] > peak and nums[i] > nums[i-1] and nums[i] > nums[i+1]:
            peak = nums[i]
            peakIndex = i
    return peakIndex

print(findPeak([0, 2, 1, 0]))