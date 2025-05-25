// Last updated: 5/25/2025, 1:08:12 PM
/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    const returnArr = [];
    for (let i=0; i<arr.length; i++){
        returnArr[i] = fn(arr[i], i);
    }
    return returnArr;
};