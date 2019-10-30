
def numTilePossibilities(tiles):
    
    result = set()

    def dfs(path, t):
        if path: # if not emptry, multiples are ok because they would overwrite anyway
            result.add(path)
        for i in range(len(t)): # this represents DFS by appending all 'other' characters
            dfs(path+t[i], t[:i]+t[i+1:])
    
    dfs('', tiles)
    return len(result)
        
result = numTilePossibilities("AAB")
print('hi')