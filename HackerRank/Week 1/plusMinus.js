function plusMinus(arr) {
  let length = arr.length;
  // Write your code here
  let positives = 0;
  let negatives = 0;
  let neutrals = 0;

  arr.map((number) =>
    number > 0 ? positives++ : number < 0 ? negatives++ : neutrals++
  );
  const values = [positives, negatives, neutrals];
  values.map((value) => console.log((value / length).toFixed(6)));
}

plusMinus([-4, 3, -9, 0, 4, 1]);
