
function arrayIntersection(nums1, nums2) {
    let result = [];
    let uniques = new Set(nums1);

    // nums1.forEach(element => {
    //     uniques.add(element);
    // }); 
    // there is probably a more elegant way to convert an array into a set
    // research shows that I can pass the array directly to the Set constructor

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