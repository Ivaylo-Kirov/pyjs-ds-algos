

function removeOuterParentheses(str) {

    l = [];
    count = 0;
    start = 0;

    for (let i = 0; i < str.length; ++i) {
        if (str[i] == "(") {
            count++;
        } else if (str[i] == ")") {
            count--;
        }
        if (count === 0) {
            l.push(str.substring(start+1, i));
            start = i + 1;
        }
    }
    return l.join('');

}

console.log(removeOuterParentheses("(()())(())"));
console.log('hi');