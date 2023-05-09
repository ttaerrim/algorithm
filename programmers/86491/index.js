function solution(sizes) {
  let w = 0;
  let h = 0;

  for (let i = 0; i < sizes.length; i++) {
    const width = Math.max(sizes[i][0], sizes[i][1]);
    const height = Math.min(sizes[i][0], sizes[i][1]);

    w = Math.max(w, width);
    h = Math.max(h, height);
  }

  return w * h;
}
