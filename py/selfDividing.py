
def selfDividing(left, right):
    result = []
    for i in range(left, right+1):
        strN = str(i)
        strL = list(strN)
        invalid = False
        for n in strL:
            if int(n) == 0:
                invalid = True
            if not invalid and i % int(n) != 0:
                invalid = True
        if not invalid:
            result.append(i)
    return result
        


print(selfDividing(1, 22))
print('hi')