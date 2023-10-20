// https://www.codewars.com/kata/5aa736a455f906981800360d/train/javascript

function feast(beast, dish) {
  let end = beast.split("").pop();
  let start = beast.split("").shift();

  return dish.split("").shift() == start && dish.split("").pop() == end;
}

function feast2(beast, dish) {
  return beast[0] === dish[0] && beast.slice(-1) === dish.slice(-1);
}

console.log(feast2("great blue heron", "garlic naan"));
