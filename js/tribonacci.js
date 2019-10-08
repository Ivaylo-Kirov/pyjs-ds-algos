
function tribonacci(n) {
    if (n == 0) {
        return 0;
    }
    if (n == 1 || n == 2) {
        return 1;
    }
    let nm3 = 0;
    let nm2 = 1;
    let nm1 = 1;
    let i = 3;
    let result = 0;
    while (i <= n) {
        result = nm3 + nm2 + nm1;
        nm3 = nm2;
        nm2 = nm1;
        nm1 = result;
        ++i;
    }
    return result;
}

