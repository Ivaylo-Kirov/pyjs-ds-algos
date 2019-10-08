
function mostFrequentChar(word) {
    const charMap = {};
    let maxNum = 0;
    let maxChar = '';

    // split word into array of chars
    // for each char, if it exists in "object map", then increment, otherwise init to 1
    word.split('').forEach((char) => {
        if (charMap[char]) {
            charMap[char]++;
        } else {
            charMap[char] = 1;
        }
    })

    // FOR IN can be used for objects
    for (char in charMap) {
        if (charMap[char] > maxNum) {
            maxNum = charMap[char];
            maxChar = char;
        }
    }
    return {maxChar, maxNum};
}

const maxObj = mostFrequentChar("javascript");
console.log(maxObj.maxChar);
console.log(maxObj.maxNum);