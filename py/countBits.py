
def countBits(num):
    nBits = 0

    while num: # while it's greater than 0
        nBits += num & 1 # compare left digit with 1
        num >>= 1 # shift to the next
    
    return nBits

result = countBits(5)