
function sumEvenAfterQueries(A, queries) {
    let evenSum = A.reduce((accum, item) => {
        return item % 2 == 0 ? accum + item : accum;
    }, 0);
    const result = [];

    for (let i = 0; i < queries.length; ++i) {
        let f = queries[i][0];
        let s = queries[i][1];
        if (A[s] % 2 == 0) {
            evenSum -= A[s];
        }
        A[s] += f;
        if (A[s] % 2 == 0) {
            evenSum += A[s];
        }
        result.push(evenSum);
    }
    return result;
}

const result = sumEvenAfterQueries([1,2,3,4], [[1,0],[-3,1],[-4,0],[2,3]]);