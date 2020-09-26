
def countDomains(L):
    resultD = dict()
    resultL = []
    for url in L:
        iResults = url.split()
        count = int(iResults[0])
        domain = iResults[1]
        

        while len(domain) > 0:
            if domain in resultD:
                resultD[domain] += count
            else:
                resultD[domain] = count

            nextDotIndex = domain.find('.')
            if nextDotIndex != -1:
                domain = domain[nextDotIndex+1:]
            else:
                break
        # good reminder of how close I was

    for m in resultD: # for each key, where m is the key (in this case it's the actual URL)
        tempStr = str(resultD[m])
        tempStr += ' '
        tempStr += m
        resultL.append(tempStr)

    return resultL


result = countDomains(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"])
print(result)