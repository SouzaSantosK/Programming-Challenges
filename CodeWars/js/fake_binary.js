// https://www.codewars.com/kata/57eae65a4321032ce000002d/solutions/javascript

function fakeBin(x) {
  let arr = x.split("");

  for (let i = 0; i < arr.length; i++) {
    arr[i] = arr[i] >= 5 ? "1" : "0";
  }

  return arr.join("");
}

function fakeBin2(x) {
  return x
    .split("")
    .map((n) => (n < 5 ? 0 : 1))
    .join("");
}

console.log(fakeBin("45385593107843568"));
console.log(fakeBin2("45385593107843568"));
