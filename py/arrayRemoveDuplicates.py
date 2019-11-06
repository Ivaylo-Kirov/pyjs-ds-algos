# Given nums = [0,0,1,1,1,2,2,3,3,4],
# Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.
# It doesn't matter what values are set beyond the returned length.

def removeDuplicates(nums):
    # result = 0

    # # confirm requirements
    # # go through my mental list of algorithm tricks
    # # explain my solution
    # # while cur = cur + 1.. keep moving.. as soon as you hit different, swap that different in the correct index, and keep moving
    # # curProcessing
    # # targetIndex
    # # iterationIndex

    # curProcessing = 0
    # targetIndex = 1
    # iterationIndex = 1

    # while targetIndex <= len(nums) - 1:
    #     while iterationIndex <= len(nums) - 1 and nums[curProcessing] >= nums[iterationIndex]: # keep moving until you find something bigger
    #         iterationIndex += 1
    #     # now I have the first index that should be swapped
    #     if iterationIndex <= len(nums) - 1:
    #         nums[targetIndex], nums[iterationIndex] = nums[iterationIndex], nums[targetIndex]
    #         curProcessing += 1
    #         targetIndex += 1
    #         iterationIndex = targetIndex
    #     else:
    #         break

    # # write pseudocode
    # # reread everything and think about edge cases and silly mistakes
    # # targetIndex now represents the last index that was succesffully clicked in
    # result = targetIndex
    # return result

    # first solution exceeded time so now trying hash

    uniqueNums = set(nums)
    nIndex = 0
    for num in sorted(uniqueNums):
        nums[nIndex] = num
        nIndex += 1

    return len(uniqueNums)

result = removeDuplicates([0,0,1,1,1,2,2,3,3,4])

print('hi')