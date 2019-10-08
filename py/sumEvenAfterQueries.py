
def sumEvenAfterQueries(A, queries):
    S = sum(x for x in A if x % 2 == 0) # initial sum
    result = []
    for first, second in queries:
        if A[second] % 2 == 0:
            S -= A[second]
        A[second] += first
        if A[second] % 2 == 0:
            S += A[second]
        result.append(S)
    return result

result = sumEvenAfterQueries([1,2,3,4], [[1,0],[-3,1],[-4,0],[2,3]])