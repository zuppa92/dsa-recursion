function isBalanced(str) {
  // Helper function to check if characters are matching pairs
  function isMatchingPair(open, close) {
    return (open === '(' && close === ')') ||
           (open === '[' && close === ']') ||
           (open === '{' && close === '}');
  }

  // Recursive function to check balance
  function checkBalance(s) {
    let openBrackets = '([{';
    let closeBrackets = ')]}';

    for (let i = 0; i < s.length; i++) {
      if (closeBrackets.includes(s[i])) {
        return false;
      }
      if (openBrackets.includes(s[i])) {
        let closeIndex = findClosingBracket(s, i);
        if (closeIndex === -1 || !isMatchingPair(s[i], s[closeIndex])) {
          return false;
        }
        // Recursively check the substring between and after the brackets
        return checkBalance(s.slice(i + 1, closeIndex)) && checkBalance(s.slice(closeIndex + 1));
      }
    }
    return true;
  }

  // Helper function to find the index of the corresponding closing bracket
  function findClosingBracket(s, openIndex) {
    let stack = 1;
    let openBrackets = '([{';
    let closeBrackets = ')]}';

    for (let i = openIndex + 1; i < s.length; i++) {
      if (openBrackets.includes(s[i])) {
        stack++;
      } else if (closeBrackets.includes(s[i])) {
        stack--;
      }
      if (stack === 0) {
        return i;
      }
    }

    return -1; // No matching closing bracket found
  }

  return checkBalance(str);
}

module.exports = isBalanced;
