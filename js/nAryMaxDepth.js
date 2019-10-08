/* // Definition for a Node.
* function Node(val,children) {
*    this.val = val;
*    this.children = children;
* };
*/

// this is almost as gold as Python's version with list comprehension
// basically you accummulate over the recursive results, but only maintaining the MAX value

var maxDepth = function(root) {
   if (!root) return 0;
   const max = root.children.reduce((max, child) => {
       return Math.max(max, maxDepth(child))
   }, 0);
   return max + 1;
};