
function reverseWords(s) {
    let sList = s.split(' ');
    let wordA = [];
    let sListR = [];
    sList.forEach((word) => {
        wordA = word.split('');
        wordA.reverse();
        word = wordA.join('');
        sListR.push(word);
    });
    const result = sListR.join(' ');
    return result;
}

const result = reverseWords("Let's take LeetCode contest");