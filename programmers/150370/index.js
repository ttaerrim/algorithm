function solution(today, terms, privacies) {
  const valids = {};

  for (let i of terms) {
    const term = i.split(" ");
    valids[term[0]] = term[1];
  }

  const answers = privacies.map((i) => {
    {
      const privacy = i.split(" ");
      const period = valids[`${privacy[1]}`];
      const date = privacy[0].split(".").map((d) => Number(d));
      date[1] += Number(period);

      if (date[1] > 12) {
        const y = Math.floor(date[1] / 12);

        date[1] = date[1] % 12;
        date[0] += y;
      }

      if (date[2] === 1) {
        date[1] -= 1;
        date[2] = 28;
      } else {
        date[2] -= 1;
      }

      if (date[1] === 0) {
        date[0] -= 1;
        date[1] = 12;
      }
      return date.join(".");
    }
  });

  const a = [];
  const answer = answers.map((i, idx) => {
    if (new Date(i) < new Date(today)) {
      a.push(idx + 1);
    }
  });

  return a;
}
