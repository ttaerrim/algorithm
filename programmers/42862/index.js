function solution(n, lost, reserve) {
  const r = reserve
    .filter((item) => lost.indexOf(item) === -1)
    .sort((a, b) => a - b);
  const l = lost
    .filter((item) => reserve.indexOf(item) === -1)
    .sort((a, b) => a - b);

  let answer = n;
  const lended = [];

  for (let i of l) {
    if (r.indexOf(i - 1) !== -1 && lended.indexOf(i - 1) === -1) {
      lended.push(i - 1);
      continue;
    }

    if (r.indexOf(i + 1) !== -1 && lended.indexOf(i + 1) === -1) {
      lended.push(i + 1);
      continue;
    }
    answer -= 1;
  }

  return answer;
}
