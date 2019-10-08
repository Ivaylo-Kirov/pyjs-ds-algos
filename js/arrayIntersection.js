
function arrayIntersection(nums1, nums2) {
    let result = [];
    let uniques = new Set();

    nums1.forEach(element => {
        uniques.add(element);
    });
    nums2.forEach(element => {
        if (uniques.has(element) && result.indexOf(element) == -1) {
            result.push(element);
        }
    });
    
    return result;
}

const result = arrayIntersection([4,9,5], [9,4,9,8,4]);
console.log('hi');



//Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
//Output: [9,4]
//Intersection means common elements
// I need to return unique list (set)