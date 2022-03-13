// 2021 카카오 채용 연계형 인턴십
// 거리두기 확인하기

function find(place) {
  const SIZE = 5;
  for (const [i, row] of place.entries()) {
    for (let j = 0; j < row.length; j++) {
      const dot = row.charAt(j);
      let p_array = [];
      if (dot === "O" || dot === "P") {
        if (i > 0) p_array = [...p_array, place[i - 1][j]];
        if (i < SIZE - 1) p_array = [...p_array, place[i + 1][j]];
        if (j > 0) p_array = [...p_array, place[i][j - 1]];
        if (j < SIZE - 1) p_array = [...p_array, place[i][j + 1]];
        const p_count = p_array.filter((element) => element === "P").length;
        if ((dot === "O" && p_count >= 2) || (dot === "P" && p_count >= 1)) {
          return false;
        }
      }
    }
  }
  return true;
}
function solution(places) {
  let answer = [];
  places.forEach((place) => {
    answer = [...answer, find(place) ? 1 : 0];
  });
  return answer;
}
