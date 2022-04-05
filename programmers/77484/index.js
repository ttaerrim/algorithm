// 로또의 최고 순위와 최저 순위

function solution(lottos, win_nums) {
  let answer = 0;
  const rank = [6, 6, 5, 4, 3, 2, 1];
  for (let i in lottos) {
    if (lottos[i] !== 0 && win_nums.includes(lottos[i])) {
      answer++;
    }
  }
  const count = lottos.filter((l) => l === 0).length;
  return [rank[answer + count], rank[answer]];
}
