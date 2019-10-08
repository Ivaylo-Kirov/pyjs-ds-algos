
def morseCode(words):
    morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

    tr = []
    count = 0
    result = ''
    ut = []

    for w in words:
        result = ''
        for i in range(len(w)):
            #print(ord(w[i]) - 97)
            #print(morse[ord(w[i]) - 97])
            result += morse[ord(w[i]) - 97]
        if len(result) > 0:
            tr.append(result)
    
    for t in tr:
        if t not in ut:
            count += 1
            ut.append(t)
    return count


morseCode(["a"])