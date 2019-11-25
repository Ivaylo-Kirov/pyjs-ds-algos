# Given an array of strings, group anagrams together.

# Example:

# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]


def groupAnagrams(strs):
    result = []
    new_strs = []
    # if I sort them individually, I can determine all anagrams
    for s in strs:
        new_strs.append(''.join(sorted(s)))
    
    dictS = dict()

    for index, s in enumerate(new_strs):
        if s in dictS:
            dictS[s].append(index)
        else:
            dictS[s] = [index]

    # then can iterate and if they match, add the index to result array
    # result dict can be dictS["aet"] = [0, 1, 2]
    for key in dictS:
        result.append([strs[ind] for ind in dictS[key]])

    return result

result = groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print('hi')