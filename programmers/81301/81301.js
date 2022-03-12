//  2021 카카오 채용연계형 인턴십 - 숫자 문자열과 영단어
function solution(s) {
  eng_num = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
  ];

  for (let i = 0; i < eng_num.length; i++) {
    s = s.split(eng_num[i]).join(i);
  }

  return Number(s);
}
