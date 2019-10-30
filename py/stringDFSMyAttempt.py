uniques = set()
def numTilePossibilities(tiles):
    # based on hint # dfs through, each unvisted combination moves dfs forward
    # store each unvisited combination into visited
    def _dfs(value, tiles):
        if value != '' and value not in uniques:
            uniques.add(value)
        for i in range(len(tiles)):
            if value+tiles[i] not in uniques:
                uniques.add(value+tiles[i])
                _dfs(value+tiles[i], tiles[:i]+tiles[i+1:])

    _dfs('', tiles)
    return len(uniques)
        
result = numTilePossibilities("AAB")
print('hi')

# my original solution needs a few tweaks, so not completely broken at least

# the leetcode solution was just more pythonic really