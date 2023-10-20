// https://www.codewars.com/kata/5264d2b162488dc400000001/train/javascript

function spinWords(string) {
  string = string.split(" ");
  let newString = [];

  for (word of string) {
    let value;
    if (word.length >= 5) {
      let copy = [];

      for (let i = word.length - 1; i >= 0; i--) {
        copy.push(word[i]);
      }

      value = copy.join("");
    } else {
      value = word;
    }
    newString.push(value);
  }

  return newString.join(" ");
}

function spinWords(string) {
  string = string.split(" ");
  let reverseString = [];

  for (word of string) {
    if (word.length >= 5) {
      let copy = word.split("").reverse().join("");
      reverseString.push(copy);
      continue;
    }
    reverseString.push(word);
  }

  return reverseString.join(" ");
}

function spinWords(string) {
  return string
    .split(" ")
    .map((word) =>
      word.length >= 5 ? word.split("").reverse().join("") : word
    )
    .join(" ");
}

console.log(spinWords("Hey fellow warriors"));
