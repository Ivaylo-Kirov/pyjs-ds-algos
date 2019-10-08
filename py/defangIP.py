
def defangIP(address):
    result = ''

    for ch in address:
        if ch == '.':
            result += '[.]'
        else:
            result += ch
    return result
    


print(defangIP('1.1.1.1'))