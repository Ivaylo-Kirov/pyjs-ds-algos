
function uncommonFromSentence(A, B) {
    let hash = {};
    const result = [];

    A.split(' ').concat(B.split(' ')).forEach((word) => {
        if (hash[word]) {
            hash[word] += 1;
        } else {
            hash[word] = 1;
        }
    });

    for (word in hash) {
        if (hash[word] < 2) {
            result.push(word);
        }
    }
    return result;
}

const result = uncommonFromSentence("this apple is sweet", "this apple is sour");