import collections, re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
        .lower().split()
        if word not in banned] # 5-10 줄을 한 줄로 줄일 수 있다
            
        count = collections.defaultdict(int) # defaultdict를 사용하는 방법......
        for word in words:
            count[word] += 1

        return max(count, key=count.get)
        # return max(count, key=(lambda k: count[k])) 
        


s = Solution()
print(s.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))
print(s.mostCommonWord("a.", []))