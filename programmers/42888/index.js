// 오픈 채팅방
function solution(record) {
  let answer = [];
  let user = {};

  record.map((r) => {
    const info = r.split(" ");
    if (info[0] !== "Leave") {
      user[info[1]] = info[2];
    }
  });

  record.map((r) => {
    const info = r.split(" ");
    if (info[0] === "Enter") {
      answer.push(user[info[1]] + "님이 들어왔습니다.");
    } else if (info[0] === "Leave") {
      answer.push(user[info[1]] + "님이 나갔습니다.");
    }
  });

  return answer;
}
