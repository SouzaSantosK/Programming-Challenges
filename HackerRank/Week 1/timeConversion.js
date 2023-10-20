function timeConversion(s) {
  s = s.split(":");
  let [hours, minutes, seconds, period] = s.map((number, index) =>
    index == 2 ? number.slice(0, 2) : index === 3 ? number.slice(2) : number
  );

  if (period == "AM")
    return `${hours == 12 ? "00" : hours}:${minutes}:${seconds}`;

  return `${hours == 12 ? hours : Number(hours) + 12}:${minutes}:${seconds}`;
}

console.log(timeConversion("04:00:00PM"));
