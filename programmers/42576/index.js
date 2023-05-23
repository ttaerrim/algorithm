function solution(participant, completion) {
  const sortedParticipant = participant.sort();
  const sortedCompletion = completion.sort();

  for (let i in sortedParticipant) {
    if (sortedParticipant[i] !== sortedCompletion[i])
      return sortedParticipant[i];
  }
}
