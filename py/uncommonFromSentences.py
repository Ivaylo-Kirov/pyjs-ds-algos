
def uncommonFromSentences(A, B):
    result = []
    hash = dict()
    for word in list(A.split(' ')):
        if word in hash:
            hash[word] += 1
        else:
            hash[word] = 1

    for word in list(B.split(' ')):
        if word in hash:
            hash[word] += 1
        else:
            hash[word] = 1

    for word in hash:
        if hash[word] < 2:
            result.append(word)
    return result

result = uncommonFromSentences("this apple is sweet", "this apple is sour")