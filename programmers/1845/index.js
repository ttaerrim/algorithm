function solution(nums) {
  const count = nums.length / 2;
  const noSameCount = Array.from(new Set(nums)).length;
  // const noSameCount = new Set(nums).size;
  return Math.min(count, noSameCount);
}
