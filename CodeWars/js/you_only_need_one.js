// https://www.codewars.com/kata/57cc975ed542d3148f00015b/train/javascript

function check(a, x) {
  return a.includes(x);
}

function check2(a, x) {
  for (item of a) {
    if (item === x) return true;
  }
  return false;
}

console.log(check2(["t", "e", "s", "t"], "e"));
