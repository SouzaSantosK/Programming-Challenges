function breakingRecords(scores) {
  let minScore = (maxScore = scores[0]);

  let minCount = (maxCount = 0);

  for (let score of scores.slice(1)) {
    if (score < minScore) {
      minScore = score;
      minCount++;
    } else if (score > maxScore) {
      maxScore = score;
      maxCount++;
    }
  }

  return [maxCount, minCount];
}

console.log(breakingRecords([9, 10, 5, 20, 20, 4, 5, 2, 25, 1]));
