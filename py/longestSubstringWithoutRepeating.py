# Given a string, find the length of the longest substring without repeating characters.

# Example 1:

# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
# Example 2:

# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

def longestSubstringLength(s):
    longest = 0
    # first idea - iterate and add to hash as you move index
    startIndex = 0
    
    while startIndex < len(s):
        cSet = set()
        curLen = 0
        iterIndex = startIndex
        while iterIndex < len(s):
            if s[iterIndex] not in cSet:
                cSet.add(s[iterIndex])
                iterIndex += 1
                curLen += 1
                longest = max(longest, curLen)
            else:
                break
        startIndex += 1
            # maintain "longest" so far
            # once you reach a char that exists in hash, break
            # increment starting index, and go again

    return longest

result = longestSubstringLength("dvdf")
print('hi')