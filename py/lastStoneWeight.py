
def lastStoneWeight(stones):

    while len(stones) > 1:
        s2 = max(stones)
        stones.remove(s2)
        s1 = max(stones)
        stones.remove(s1)
        if s1 == s2:
            continue
        else:
            stones.append(s2 - s1)

    if len(stones) > 0:
        return stones[0]
    else:
        return 0


result = lastStoneWeight([2,7,4,1,8,1])