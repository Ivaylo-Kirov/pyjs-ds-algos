
def removeOuterParentheses(S):
    
    l = []
    count = 0
    start = 0

    for i in range(len(S)):
        if S[i] == "(":
            count += 1
        elif S[i] == ")":
            count -= 1
        if count == 0:
            l.append(S[start+1:i])
            start = i + 1
    return "".join(l)


print(removeOuterParentheses("(()())(())(()(()))"))