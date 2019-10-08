
function selfDividing(left, right) {
    let invalid = false;
    const result = [];
    for (let i = left; i <= right; ++i) {
        const strN = i.toString();
        const strA = strN.split('');
        invalid = false;
        
        strA.forEach((c) => {
            if (c == 0) {
                invalid = true;
            }
            if (i % parseInt(c) != 0) {
                invalid = true;
            }
        });
        if (invalid != true ) {
            result.push(i);
        }
    }
    return result;
}

console.log(selfDividing(1, 22));
console.log('hi');