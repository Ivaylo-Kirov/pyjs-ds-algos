
# a-z : stands for itself
# . : matches any character
# * : matches 0 or more occurrences of the previous single character
def RegExEval(s, p):
    # keep track of indecies for each
    si = 0
    pi = 0
    while si < len(s) and pi < len(p):
        if p[pi] == '.' or s[si] == p[pi]:
            if pi + 1 < len(p):
                if p[pi+1] == '*':
                    # special case with multiples
                    pi += 2 # move past star
                    while si + 1 < len(s) and s[si] == s[si+1]: # keep moving index while there is a match (e.g. same character)
                        si += 1
                    si += 1
                else:
                    si += 1
                    pi += 1
            else: 
                si += 1
                pi += 1
        else: # they don't match
            if pi + 1 < len(p):
                if p[pi+1] == '*':
                    # special case with multiples
                    pi += 2
                    si += 1
                else:
                    return False
            else:
                return False
        



    #   if pattern + 1 is *, then consider them together
    #   else compare pattern value to string value
    #       if they match, keep going
    #       else return False

    if pi < len(p) and p[pi] != '.':
        # still something left to match, so return False unless it's a dot
        return False
    if si < len(s):
        return False
    return True

# examples:
# "aba" | pattern "ab" | False
# "aa" | pattern "a*" | True
# "ab" | p = ".*" | True
# "ab" | p = "." | False
# "aab" | pattern "c*a*b" | True
# "aaa" | pattern "a*." | True

result = RegExEval("aaa", "a*.")
print('hi')