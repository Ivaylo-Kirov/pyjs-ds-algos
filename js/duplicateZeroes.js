
const duplicateZeroes = (arr) => {
    let i = 0;
    let dup = arr;

    while (i < dup.length - 1) {
        if (dup[i] == 0) {
            dup = dup.slice(0, i+1).concat(dup.slice(i, i + 1)).concat(dup.slice(i+1, dup.length - 1));
            i++;
        }
        i++;
    }
    if (arr != dup) {
        arr.splice(0, arr.length);
        for (d in dup) {
            arr.push(dup[d]);
        }
    }
}

duplicateZeroes([1,0,2,3,0,4,5,0]);

/*
i = 0
        dup = arr
        while i < len(dup) - 1:
            if dup[i] == 0:
                dup = dup[:i+1] + [0] + dup[i+1:len(dup) - 1]
                i += 1
            i += 1
        if arr != dup:
            arr.clear()
            for d in dup:
                arr.append(d)
*/