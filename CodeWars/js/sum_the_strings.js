// https://www.codewars.com/kata/5966e33c4e686b508700002d/train/javascript

function sumStr(a, b) {
  return "" + (+a + +b);
}

function sumStr2(a, b) {
  return String(Number(a) + Number(b));
}

console.log(sumStr2("4", "5"));
