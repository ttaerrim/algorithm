function fillNumber(num) {
  return Number(num.toString().repeat(4).slice(0, 4));
}

function solution(numbers) {
  const answer = numbers
    .sort((a, b) => {
      return fillNumber(b) - fillNumber(a);
    })
    .join("");

  return BigInt(answer).toString();
}
