# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.

# Example 1:

# Input: "()"
# Output: true
# Example 2:

# Input: "()[]{}"
# Output: true
# Example 3:

# Input: "(]"
# Output: false

def matchingParentheses(s):
    
    stk = []

    for ch in s:
        if ch == '(':
            stk.append(ch)
            continue
        if ch == ')':
            if len(stk) == 0:
                return False
            if stk[-1] == '(':
                stk.pop()
                continue
            else:
                return False
        
        if ch == '[':
            stk.append(ch)
            continue
        if ch == ']':
            if len(stk) == 0:
                return False
            if stk[-1] == '[':
                stk.pop()
                continue
            else:
                return False

        if ch == '{':
            stk.append(ch)
            continue
        if ch == '}':
            if len(stk) == 0:
                return False
            if stk[-1] == '{':
                stk.pop()
                continue
            else:
                return False
    
    if len(stk) > 0:
        return False
    return True

result = matchingParentheses("(")
print('hi')