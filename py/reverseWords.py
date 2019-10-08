
def reverseWords(str):
    strL = str.split(' ')
    strLR = []
    strResult = ""
    for word in strL:
        strLR.append(word[::-1])
    for word in strLR:
        strResult += word + " "
    return strResult


result = reverseWords("let's leetcode")