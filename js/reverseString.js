
function reverseString(str) {
    // turn string into an array
    let strArr = str.split('');
    strArr.reverse();
    // convert array back to string
    let newStr = strArr.join('');
    console.log(newStr);
}

reverseString("hello");