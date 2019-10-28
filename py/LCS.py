def LCS(s1, s2, i1 = 0, i2 = 0):
    if i1 >= len(s1):
        return []
    if i2 >= len(s2):
        return []

    if s1[i1] == s2[i2]:
        return [s1[i1]] + LCS(s1, s2, i1 + 1, i2 + 1)
    else:
        return max(LCS(s1, s2, i1 + 1, i2), LCS(s1, s2, i1, i2 + 1), key=len)

s1 = 'ABAZDC'
s2 = 'BACBAD'


result = ''.join(LCS(s1, s2))
print('hi')

# base example works, but now how do I return the actual string that represents the LCS?
# had almost an epiphany by replacing 0 with [] and doing the max based on length and it worked
# this would break of course for larger strings due to recursion
