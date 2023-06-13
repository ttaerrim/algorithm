function solution(clothes) {
  const result = {};

  for (let item of clothes) {
    if (result[item[1]]) {
      result[item[1]].push(item[0]);
    } else {
      result[item[1]] = [item[0]];
    }
  }

  const res = Object.values(result).map((item) => item.length);
  return res.reduce((arr, item) => arr * (item + 1), 1) - 1;
}
