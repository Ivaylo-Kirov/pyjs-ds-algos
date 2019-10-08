
def findOccurrences(text, first, second):
    result = []
    textL = text.split(' ')

    for i in range(len(textL)-2):
        if textL[i] == first and textL[i+1] == second:
            result.append(textL[i+2])
            if (i + 2 < len(textL)-2):
                i += 2
            else:
                break



    return result


result = findOccurrences("ypkk lnlqhmaohv lnlqhmaohv lnlqhmaohv ypkk ypkk ypkk ypkk ypkk ypkk lnlqhmaohv lnlqhmaohv lnlqhmaohv lnlqhmaohv ypkk ypkk ypkk lnlqhmaohv lnlqhmaohv ypkk", "lnlqhmaohv", "ypkk")
print('hi')
