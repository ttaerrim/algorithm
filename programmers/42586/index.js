function solution(progresses, speeds) {
  const days = [];
  const answer = [];

  for (let i in progresses) {
    days.push(Math.ceil((100 - progresses[i]) / speeds[i]));
  }

  let most = days[0];
  let j = 0;
  for (let i of days) {
    if (most < i) {
      answer.push(j);
      most = i;
      j = 1;
      continue;
    }
    j += 1;
  }
  answer.push(j);

  return answer;
}
