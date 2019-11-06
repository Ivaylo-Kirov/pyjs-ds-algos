def longestPalindromeSubseq(s):
    
    result = 0

    # squeeze and recurse on (start + 1) and (end - 1) routes

    # if start == end.. +2 to result + recurse

    # else max(recurse1, recurse2)

    def _longestPalindromeSubseq(s, start, end):
        if start > end:
            return 0
        if start == end:
            return 1
        if s[start] == s[end]:
            return 2 + _longestPalindromeSubseq(s, start+1, end-1)
        else:
            return max(_longestPalindromeSubseq(s, start, end-1), _longestPalindromeSubseq(s, start+1, end))

    result = _longestPalindromeSubseq(s, 0, len(s)-1)
    return result

    # I ran it and it's too slow, its runtime is factorial 2*n, but I am not sure exactly why
    # to be better next time, when I get stuck like this, go over the clues
    # hash - dp - sort - stack - queue - divide



result = longestPalindromeSubseq("a")
print('hi')
# Example 1:
# Input:

# "bbbab"
# Output:
# 4
# One possible longest palindromic subsequence is "bbbb".
# Example 2:
# Input:

# "cbbd"
# Output:
# 2
# One possible longest palindromic subsequence is "bb".