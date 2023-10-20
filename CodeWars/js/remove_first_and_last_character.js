// https://www.codewars.com/kata/56bc28ad5bdaeb48760009b0/train/javascript

function removeChar(str) {
  return str.slice(1, -1);
}

function removeChar(str) {
  let str1 = str.split("");
  str1.shift();
  str1.pop();
  return str1;
}

console.log(removeChar("eloquent"));
