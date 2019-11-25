# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Note:
# The solution set must not contain duplicate triplets.

# Example:
# Given array nums = [-1, 0, 1, 2, -1, -4],

# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

def three_sum(nums):
    result3 = []

    # hash
    # iterate, and do 2 sum over the rest - linear + linear so N2

    def two_sum(numst, target):
        result = []
        dictS = dict()
        for num in numst:
            if num in dictS:
                dictS[num] += 1
            else:
                dictS[num] = 1

        for num in numst:
            temp_target = target - num

            if num == temp_target and dictS[temp_target] < 2:
                continue
            else:
                if temp_target in dictS and dictS[temp_target] > 0:
                    result.append([num, temp_target])
                    dictS[num] -= 1
                    dictS[temp_target] -= 1

        return result

    for index, num in enumerate(nums):
        results = two_sum(nums[:index] + nums[index+1:], 0 - num)
        for result in results: # results should now hold a list of lists of matching 2 sums
            result3.append(result + [num])


    # manual sort to remove duplicates?
    for r in result3:
        r.sort()
    result3.sort()
    original_length = len(result3)
    curi = 1
    while curi < original_length:
        if curi < len(result3):
            if result3[curi-1] == result3[curi]:
                result3 = result3[:curi-1] + result3[curi:]
                curi -= 1
            curi += 1
        else:
            break

    return result3

# it worked, but officially time limit exceeded
# online solutions also use N2, so I think what failed me is the last "custom" removal of duplicates which does way more n*n log n processes.. moving on for now

result = three_sum([-1, 0, 1, 2, -1, -4])
print('hi')