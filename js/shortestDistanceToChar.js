
function shortestDistanceToChar(S, C) {
    let result = [];
    let prev = -100000;

    for (let i = 0; i < S.length; ++i) {
        if (S[i] == C) {
            prev = i;
        }
        result.push(i - prev);
    }

    prev = 100000;
    for (let i = S.length - 1; i >= 0; --i) {
        if (S[i] == C) {
            prev = i;
        }
        result[i] = Math.min(result[i], prev - i);
    }


    return result;

}

const result = shortestDistanceToChar("loveleetcode", 'e')