
function capitalizeLetters(sentence) {
    const wordArray = sentence.toLowerCase().split(' ');
    for (let i = 0; i < wordArray.length; ++i) {
        wordArray[i] = wordArray[i].substring(0, 1).toUpperCase() + wordArray[i].substring(1);
    }
    return wordArray.join(' ');
}

function capitalizeLettersWithMap(sentence) {
    return sentence.toLowerCase().split(' ').map((word) => {
        return word[0].toUpperCase() + word.substring(1);
    }).join(' ');
}

console.log(capitalizeLetters("i love javascript"));
console.log(capitalizeLettersWithMap("i love javascript"));