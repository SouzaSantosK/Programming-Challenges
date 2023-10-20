// https://www.codewars.com/kata/56efc695740d30f963000557/train/javascript

String.prototype.toAlternatingCase = function () {
  str = this.split("");

  for (i = 0; i < str.length; i++) {
    if (str[i].toUpperCase() === str[i]) {
      str[i] = str[i].toLowerCase();
    } else {
      str[i] = str[i].toUpperCase();
    }
  }

  return str.join("");
};

String.prototype.toAlternatingCase2 = function () {
  return this.split("")
    .map((char) =>
      char === char.toUpperCase() ? char.toLowerCase() : char.toUpperCase()
    )
    .join("");
};

console.log("1a2b3c4d5e".toAlternatingCase2());
