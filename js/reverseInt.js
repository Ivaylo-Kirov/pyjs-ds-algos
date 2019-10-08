
const reverseInt = (int) => {
    const revStr = int.toString().split('').reverse().join('');
    return parseInt(revStr);
    // above can be * by Math.sign(int) to handle negatives
}

console.log(reverseInt(123));