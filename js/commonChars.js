function commonChars(A) {
    let AMap = {};
    let result = [];
    let ASet = new Set()
    for (let i = 0; i < A[0].length; ++i) {
        ASet.add(A[0][i]);
    }

    for (ch of ASet) {
        AMap[ch] = count(A[0], ch);
    }

    for (word of A) {
        for (ch of ASet) {
            if (count(word, ch)) {
                AMap[ch] = Math.min(count(word, ch), AMap[ch]);
            } else {
                if (AMap.hasOwnProperty(ch)) {
                    delete AMap[ch];
                }
            }
        }
    }

    for (let ch in AMap) {
        for (let i = 0; i < AMap[ch]; ++i) {
            result.push(ch);
        }
    }

    return result;

}

function count(str, val) {
    let counter = 0;
    for (let i = 0; i < str.length; ++i) {
        if (str[i] == val) {
            counter++;
        }
    }
    return counter;
}

const result = commonChars(["bella","label","roller"]);
console.log('hi');