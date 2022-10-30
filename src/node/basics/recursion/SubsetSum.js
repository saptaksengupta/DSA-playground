/**
 * Print list of all subset sum of a given array
 * Example: [3,1,2] -> sum{} -> 0, sum{3} -> 3, sum{1} -> 1, sum{3,1} -> 4 ... 
 * Output: [6,4,5,3,3,1,2,0] 
 */
function getSubsetSum(index, sum, subset, array) {
    if (array.length == index) {
        subset.push(sum);
        return;
    }

    getSubsetSum(index+1, sum + array[index], subset, array);

    getSubsetSum(index + 1, sum, subset, array);
}

var array = [3,1,2];
var subset = [];
getSubsetSum(0, 0, subset, array);
console.log(subset);
