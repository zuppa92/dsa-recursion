const product = require('./product');

test('calculates the product of an array of numbers', () => {
    expect(product([2, 3, 4])).toBe(24);
    expect(product([1, 2, 3, 4, 5])).toBe(120);
    expect(product([10])).toBe(10);
    expect(product([])).toBe(1); // Product of an empty array is 1
});
