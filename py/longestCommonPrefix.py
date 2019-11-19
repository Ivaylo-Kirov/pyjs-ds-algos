# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

def longestCommonPrefix(strs):
    if len(strs) == 0:
        return ''
    curMax = strs[0]

    # loop through all strs - 1:end
    for word in strs:
        if len(word) == 0:
            return ''
        # iterate through string chars and check if curMax can be maintained or needs to be reduced
        for i in range(len(word)):
            # for each character, compare it with matching index inside curMax
            if i < len(curMax) and word[i] != curMax[i]:
                # if they match, keep the word iteration going
                # # if they don't match, set new curMax, and break
                curMax = curMax[0:i]
                if i == 0:
                    return curMax
                break
        endIndex = min(len(curMax), len(word))
        curMax = curMax[0:endIndex]

    return curMax


result = longestCommonPrefix(["aaa","aa","aaa"])
print('hi')