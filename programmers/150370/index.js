function solution(today, terms, privacies) {
  const valids = {};

  const [ty, tm, td] = today.split(".").map(Number);
  const todayNum = ty * 12 * 28 + tm * 28 + td;

  for (let i of terms) {
    const [type, period] = i.split(" ");
    valids[type] = Number(period);
  }

  const a = [];
  const answers = privacies.map((i) => {
    {
      const [date, type] = i.split(" ");

      const period = valids[type];
      const [y, m, d] = date.split(".").map(Number);

      return y * 12 * 28 + m * 28 + d + Number(period) * 28;
    }
  });

  answers.forEach((i, idx) => {
    if (i <= todayNum) {
      a.push(idx + 1);
    }
  });

  return a;
}
