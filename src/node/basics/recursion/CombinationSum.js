/**
 * Print all combinations of a given array having sum K.
 * EX: [2,3,6,7] => [[2,2,3], [7]]
 */

function getAllCombinations(index, sum, ds, len) {
    if (index == len) {
        if (sum == 0) {
            resArray.push([...ds]);
        }
        return;
    }

    if (sum >= array[index]) {
        ds.push(array[index]);
        getAllCombinations(index, sum - array[index], ds, len);
        ds.splice(ds.length - 1);
    }

    getAllCombinations(index + 1, sum, ds, len);
}


var array = [2,3,6,7];
var sum = 7;
var resArray = [];
getAllCombinations(0, sum, [], array.length);
console.log(resArray);