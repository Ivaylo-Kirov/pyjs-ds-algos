
function defangIP(address) {
    let newAddress = address.split('').map((char) => {
        if (char === '.') {
            char = '[.]';
        }
        return char;
    });
    return newAddress.join('');
}

console.log(defangIP('1.1.1.1'));