
const lastStoneWeight = (stones) => {
    while (stones.length > 1) {
        let s2 = Math.max(...stones);
        stones.splice(stones.indexOf(s2), 1);
        let s1 = Math.max(...stones);
        stones.splice(stones.indexOf(s1), 1);
        if (s1 == s2) {
            continue;
        } else {
            stones.push(s2 - s1);
        }
    }
    return stones.length > 0 ? stones[0] : 0;
}

const result = lastStoneWeight([2, 7, 4, 1, 8, 1]);