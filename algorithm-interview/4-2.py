import collections, re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
        .lower().split()
        if word not in banned] # 5-10 줄을 한 줄로 줄일 수 있다
            
        count = collections.Counter(words) # defaultdict를 사용하는 방법......
        return count.most_common(1)[0][0] # most_common은 빈도수가 높은 순으로 반환한다. 괄호 안에는 반환할 튜플의 개수
        


s = Solution()
print(s.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))
print(s.mostCommonWord("a.", []))