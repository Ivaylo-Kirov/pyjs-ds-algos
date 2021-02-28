
function validateSubsequence(array, sequence) {
    let curMatching = 0;
    for (let i = 0; i < array.length; ++i) {
        if (array[i] == sequence[curMatching]) {
            curMatching++;
        }
    }
    if (curMatching < sequence.length) {
        return false;
    }
    return true;
}

let result = validateSubsequence([1, 3, 4, 2], [1, 4, 2]);