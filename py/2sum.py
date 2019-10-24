
def two_sum(L, goal):

    seen = set()
    result = []

    for num in L:
        target = goal - num
        if target in seen:
            result.append((num, target))
        else:
            seen.add(num)
    return result

result = two_sum([1, 3, 2, 5, 2], 4)
print(result)