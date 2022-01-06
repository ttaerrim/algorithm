//  평균 구하기
function solution(arr) {
  var answer = arr.reduce((p, c) => p + c, 0) / arr.length;
  return answer;
}
