function miniMaxSum(arr) {
  let maxValue = Math.max(...arr);
  let minValue = Math.min(...arr);

  let maxSum = arr.reduce((sum, current) => sum + current, -minValue);
  let minSum = arr.reduce((sum, current) => sum + current, -maxValue);

  console.log(`${minSum} ${maxSum}`);
}

// Outra solução

function miniMaxSum(arr) {
  arr.sort((a, b) => a - b);

  let minSum = arr.slice(0, 4).reduce((sum, current) => sum + current, 0);
  let maxSum = arr.slice(1).reduce((sum, current) => sum + current, 0);
  console.log(`${minSum} ${maxSum}`);
}

miniMaxSum([1, 2, 3, 4, 5]);
