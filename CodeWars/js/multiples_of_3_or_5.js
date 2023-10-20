// https://www.codewars.com/kata/514b92a657cdc65150000006/train/javascript

function solution(number) {
  if (number < 0) return 0;
  let arr = [];

  for (let i = 1; i < number; i++) {
    if (i % 3 == 0 || i % 5 == 0) {
      arr.push(i);
    }
  }

  return arr.reduce((sum, current) => sum + current, 0);
}

function solution(number) {
  let sum = 0;

  for (let i = 3; i < number; i++) {
    if (i % 3 == 0 || i % 5 == 0) {
      sum += i;
    }
  }

  return sum;
}

console.log(solution(0));
