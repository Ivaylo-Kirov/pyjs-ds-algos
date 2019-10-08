
function removeDuplicates(S) {

    let madeRevisions = true
    
    while (madeRevisions == true) {
        madeRevisions = false
        for (let i = 0; i < S.length; ++i) {
            if (i < S.length - 1 && S[i] == S[i+1]) {
                madeRevisions = true
                S = S.substr(0, i) + S.slice(i+2)
            }
        }
    }
                
    return S
}


result = removeDuplicates("abbacaddeegh")