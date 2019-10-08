
function findOccurrences(text, first, second) {
    const result = [];
    const textA = text.split(' ');

    for (let i = 0; i < textA.length - 1; ++i) {
        if (textA[i] == first && textA[i+1] == second) {
            if (i + 2 < textA.length) {
                result.push(textA[i+2]);
            }
        }
        
    }
    return result;
}

const result = findOccurrences("alice is a good girl she is a good student", "a", "good");
console.log('hi');