
function morseCode(words) {

    const morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

    const ut = new Set();

    words.forEach((w) => {
        let result = '';
        for (let i = 0; i < w.length; ++i) {
            //console.log(w.charCodeAt(i) - 97);
            result += morse[w.charCodeAt(i) - 97];
        }
        ut.add(result);
    })
    return ut.size;
    
}

morseCode(["ab", "cd"])