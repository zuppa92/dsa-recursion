const isBalanced = require('./balancedBrackets');

describe("isBalanced", function() {
  it("returns true for balanced strings", function() {
    expect(isBalanced("hello")).toBe(true);
    expect(isBalanced("(hi) [there]")).toBe(true);
    expect(isBalanced("(hi [there])")).toBe(true);
    expect(isBalanced("(((hi)))")).toBe(true);
  });

  it("returns false for imbalanced strings", function() {
    expect(isBalanced("(hello")).toBe(false);
    expect(isBalanced("(nope]")).toBe(false);
    expect(isBalanced("((ok) [nope)]")).toBe(false);
  });
});
