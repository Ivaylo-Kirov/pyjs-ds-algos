import random
def manual_shuffle(S):
    rList = [""] * len(S)
    seen = set()
    
    for ch in S:
        keep_going = True
        while keep_going:
            rInt = random.randint(0, len(S)-1)
            if rInt in seen:
                keep_going = True
                continue
            seen.add(rInt)
            keep_going = False

        rList[rInt] = ch

    return ''.join(rList)


# test randomness
def test_randomness():
    S = 'abcdef'
    a_locs = dict()
    for _ in range(0, 1000):
        result = manual_shuffle(S)
        a_pos = result.find(S[0])
        if a_pos in a_locs:
            a_locs[a_pos] += 1
        else:
            a_locs[a_pos] = 1
    
    for k, v in a_locs.items():
        print('location results: ' + str(k) + ' occurred ' + str(v) + ' times')

#print(manual_shuffle('abcdef'))

print(test_randomness())

print('hi')