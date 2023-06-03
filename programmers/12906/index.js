function solution(arr) {
  var answer = [];
  let prev = -1;
  for (let i = 0; i < arr.length; i++) {
    if (prev !== arr[i]) {
      answer.push(arr[i]);
    }
    prev = arr[i];
  }

  return answer;
}
