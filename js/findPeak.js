
function findPeak(A) {
    let peak = 0;
    let peakIndex = 0;
    for (let i = 0; i < A.length; ++i) {
        if (A[i] > peak && A[i] > A[i-1] && A[i] > A[i+1]) {
            peak = A[i];
            peakIndex = i;
        }
    }
    return peakIndex;
}

console.log(findPeak([0, 2, 1, 0]));
console.log('hi');