
def tribonacci(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    nm3 = 0
    nm2 = 1
    nm1 = 1
    i = 3
    result = 0
    while i <= n:
        result = nm3 + nm2 + nm1
        nm3 = nm2
        nm2 = nm1
        nm1 = result
        i += 1
    return result

result = tribonacci(4)