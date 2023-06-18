function solution(arr) {
  const counts = arr.reduce((obj, item) => {
    obj[item] = obj[item] ? obj[item] + 1 : 1;
    return obj;
  }, {});

  const res = Object.values(counts).filter((item) => item !== 1);

  if (res.length === 0) {
    return [-1];
  } else return res;
}

solution([12, 3, 4, 12]);
