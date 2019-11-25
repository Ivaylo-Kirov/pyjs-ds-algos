def letterCasePermutation(S):
    # empty list with one char
    res = ['']
    # iterate
    for ch in S:
        if ch.isalpha():
            result = [i+j for i in res for j in [ch.upper(), ch.lower()]]
        else:
            result = [i+ch for i in res]
    #check if isalpha():
    # if yes, list comprehension i+j (i is all existing res values) j is list of upper/lower of ch
    # if not, list comprehension +ch
    return result

result = letterCasePermutation("a1b2")

#["a1b2", "a1B2", "A1b2", "A1B2"]


# this didn't make any sense at first 'copied from leetcode answers'
# but later I read it again after I understood how the 'product' of 2 values can be done in a list comprehension
# and so it kind of dinged