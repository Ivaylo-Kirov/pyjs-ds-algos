
const isPalindrome = (str) => {
    const revStr = str.split('').reverse().join('');
    return revStr === str;
}

console.log(isPalindrome("racecar"));