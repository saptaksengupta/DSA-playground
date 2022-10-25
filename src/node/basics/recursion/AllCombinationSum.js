/**
 * Printing all Sub sequences where sum is K
 * Example: [1,2,1], Sum = 2
 */


function allCombination(index, ds, array, s, n, sum) {
    if (index == n) {
        if (sum == s) {
            console.log(ds);
        }
        return;
    }

    ds.push(array[index]);
    s += array[index];
    allCombination(index + 1, ds, array, s, n, sum);
    
    s -= array[index];
    ds.splice(ds.length - 1);
    allCombination(index + 1, ds, array, s, n, sum);
}

const array = [1,2,1];
const ds = [];

// console.log(allCombination(0, ds, array, 0, 3, 2));

/**
 * Printing any one Sub sequence where sum is K
 * Example: [1,2,1], Sum = 2
 */


 function oneCombination(index, ds, array, s, n, sum) {
    if (index == n) {
        if (sum == s) {
            return true;
        } else {
            return false;
        }
    }

    ds.push(array[index]);
    s += array[index];
    var l = oneCombination(index + 1, ds, array, s, n, sum);
    if (l == true) {
        return true;
    }
    s -= array[index];
    ds.splice(ds.length - 1);
    var r = oneCombination(index + 1, ds, array, s, n, sum);
    if (r == true) {
        return true;
    }

    return false;
}

// console.log(oneCombination(0, ds, array, 0, 3, 2) ? ds : false);

/**
 * Printing number of Sub sequence where sum is K
 * Example: [1,2,1], Sum = 2
 */


 function getNumberOfCombination(index, ds, array, s, n, sum) {
    if (index == n) {
        if (sum == s) {
            return 1;
        } else {
            return 0;
        }
    }

    ds.push(array[index]);
    s += array[index];
    var l = getNumberOfCombination(index + 1, ds, array, s, n, sum);

    s -= array[index];
    ds.splice(ds.length - 1);
    var r = getNumberOfCombination(index + 1, ds, array, s, n, sum);
    

    return l + r;
}

console.log(getNumberOfCombination(0, ds, array, 0, 3, 2));