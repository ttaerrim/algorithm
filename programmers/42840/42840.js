// 모의고사
function solution(answers) {
  var answer = [];
  let score = [0, 0, 0];
  const patterns = [
    [1, 2, 3, 4, 5],
    [2, 1, 2, 3, 2, 4, 2, 5],
    [3, 3, 1, 1, 2, 2, 4, 4, 5, 5],
  ];

  answers.forEach((num, idx) => {
    if (num === patterns[0][idx % patterns[0].length]) {
      score[0] += 1;
    }
    if (num === patterns[1][idx % patterns[1].length]) {
      score[1] += 1;
    }
    if (num === patterns[2][idx % patterns[2].length]) {
      score[2] += 1;
    }
  });

  for (let i = 0; i < score.length; i++) {
    if (score[i] === Math.max(...score)) {
      answer.push(i + 1);
    }
  }

  return answer;
}

function solution(answers) {
  const supojas = [
    [1, 2, 3, 4, 5],
    [2, 1, 2, 3, 2, 4, 2, 5],
    [3, 3, 1, 1, 2, 2, 4, 4, 5, 5],
  ];

  const answerCount = [0, 0, 0];
  const answer = [];

  for (let i in answers) {
    supojas.forEach((_, idx) => {
      if (answers[i] === supojas[idx][i % supojas[idx].length]) {
        answerCount[idx] += 1;
      }
    });
  }

  for (let i = 0; i < answerCount.length; i++) {
    if (answerCount[i] === Math.max(...answerCount)) {
      answer.push(i + 1);
    }
  }

  return answer;
}
