# Evaluate the value of an arithmetic expression in Reverse Polish Notation.

# Valid operators are +, -, *, /. Each operand may be an integer or another expression.

# Input: ["2", "1", "+", "3", "*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
# Example 2:

# Input: ["4", "13", "5", "/", "+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6

def evalRPN(tokens):
    result = 0

    # my thoughts were:
    # stack, keep going until you meet +, -, *, / then apply it to 2 previous entries in stack, and slice the result into those 3 spaces
    stk = []
    signs = ['+', '-', '*', '/']
    i = 0
    j = 0 # stk index
    original_length = len(tokens)

    while i < original_length and j < original_length:
        if tokens[i] in signs:
            mSign = signs.index(tokens[i])
            # do the math and slice it in
            if mSign == 0: # addition
                tempResult = int(stk[j-2]) + int(stk[j-1])
                stk[j-2:] = [str(tempResult)]
                j -= 2
            if mSign == 1: # subtraction
                tempResult = int(stk[j-1]) - int(stk[j-2])
                stk[j-2:] = [str(tempResult)]
                j -= 2
            if mSign == 2: # multiplication
                tempResult = int(stk[j-1]) * int(stk[j-2])
                stk[j-2:] = [str(tempResult)]
                j -= 2
            if mSign == 3: # division
                tempResult = int(stk[j-2]) // int(stk[j-1])
                stk[j-2:] = [str(tempResult)]
                j -= 2
        else:
            stk.append(tokens[i])
        i += 1
        j += 1

    return int(stk[0])

# mostly worked and I got my lessons, maintaining 2 indexes again, using a stack

result = evalRPN(["2", "1", "+", "3", "*"])
print('hi')