function product(arr) {
    if (arr.length === 0) return 1; // Base case: product of empty array is 1
    return arr[0] * product(arr.slice(1)); // Recursive case
}

module.exports = product;
