// https://www.codewars.com/kata/5808dcb8f0ed42ae34000031/train/javascript

function switchItUp(number) {
  let numbers = [
    "Zero",
    "One",
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
  ];

  return numbers[number];
}

// Ou

switchItUp = (n) =>
  [
    "Zero",
    "One",
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
  ][n];

console.log(switchItUp(0));
