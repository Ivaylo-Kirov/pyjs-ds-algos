
def shortestToChar(S, C):
    result = []
    prev = float('-inf')

    # enumerate
    # for counter, value in enumerate(some_list)

    for counter, value in enumerate(S):
        if value == C: 
            prev = counter
        result.append(counter - prev)

    # float('-inf')
    # lower bound

    #float('inf')
    # upper bound

    prev = float('inf')
    # backwards
    for i in range(len(S) - 1, -1, -1):
        # now compare result[i] to existing value from forward iteration
        if S[i] == C:
            prev = i
        result[i] = min(result[i], prev - i)

    return result


result = shortestToChar("loveleetcode", 'e')