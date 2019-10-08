
const nextGreaterElement = (nums1, nums2) => {
    let result = [];
    for (num in nums1) {
        let foundIndex = nums2.indexOf(nums1[num]);
        let found = false;
        if (foundIndex == -1) {
            break;
        } else {
            for (let i = foundIndex + 1; i < nums2.length; ++i) {
                if (nums2[i] > nums1[num]) {
                    result.push(nums2[i]);
                    found = true;
                    break;
                }
            }
        }
        if (found != true) {
            result.push(-1);
        }
    }
    return result;
}

const result = nextGreaterElement([4, 1, 2], [1, 3, 4, 2]);