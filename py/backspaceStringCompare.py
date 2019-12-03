# Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

# Example 1:

# Input: S = "ab#c", T = "ad#c"
# Output: true
# Explanation: Both S and T become "ac".
# Example 2:

# Input: S = "ab##", T = "c#d#"
# Output: true
# Explanation: Both S and T become "".
# Example 3:

# Input: S = "a##c", T = "#a#c"
# Output: true
# Explanation: Both S and T become "c".
# Example 4:

# Input: S = "a#c", T = "b"
# Output: false
# Explanation: S becomes "c" while T becomes "b".

def backspaceCompare(S, T):

    def solve(pStr):
        newStr = ""

        for ch in pStr:
            if ch == "#":
                # cut it
                newStr = newStr[:-1]
            else:
                newStr += ch

        return newStr

    return solve(S) == solve(T)


result = backspaceCompare("ab#c", "ad#c")
print('hi')