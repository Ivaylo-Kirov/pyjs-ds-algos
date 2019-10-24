def missingItem(L1, L2):
    
    # brute force # N2
    # for elem in L1:
    #     if elem not in L2:
    #         missing_item = elem

    # slightly faster # N log N
    # shorter, longer = sorted([L1, L2], key=len)
    # seen = set(shorter)
    
    # for elem in longer:
    #     if elem not in seen:
    #         return elem
    
    # crazy python sets way
    #return set(L1).difference(set(L2))

    

print(missingItem([4, 9, 5, 16], [4, 9, 16]))

print('hi')