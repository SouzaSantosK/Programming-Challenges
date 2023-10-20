// https://www.codewars.com/kata/51b6249c4612257ac0000005/train/javascript

function solution(roman) {
  const romanNumbers = {
    I: 1,
    V: 5,
    X: 10,
    L: 50,
    C: 100,
    D: 500,
    M: 1000,
  };
  let result = 0;

  for (let i = 0; i < roman.length; i++) {
    console.log(roman[i], romanNumbers[roman[i]]);
    const currentSymbol = roman[i];
    const currentValue = romanNumbers[currentSymbol];
    const nextSymbol = roman[i + 1];
    const nextValue = romanNumbers[nextSymbol];

    if (nextValue && nextValue > currentValue) {
      result += nextValue - currentValue;
      i++;
    } else {
      result += currentValue;
    }
  }
  return result;
}

console.log(solution("IV"));
