# Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

# Examples:

# s = "leetcode"
# return 0.

# s = "loveleetcode",
# return 2.
# Note: You may assume the string contain only lowercase letters.

def firstUniqChar(s):
    result = -1

    # easy n2 solution is to start at each character iterate until the end

    # what if I use a dict with counts?

    dictS = dict()

    for ch in s:
        if ch not in dictS:
            dictS[ch] = 1
        else:
            dictS[ch] += 1

    for key in dictS: # this iterates in order they were inserted
        if dictS[key] == 1: # if it only appeared once
            return s.index(key)
    

    return result

result = firstUniqChar("leetcode")
print('hi')