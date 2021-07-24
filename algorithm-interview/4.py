import collections, re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        paragraph=paragraph.lower()
        paragraph = re.sub('[^a-z_ ]', '', paragraph).split()
        
        if banned is not None:
            for i in banned:
                paragraph.remove(i) # leetcode 상에서는 여기서 오류가 났다
            
        count = collections.Counter(paragraph)
        max_value = max(list(count.values()))
        for key in list(count.keys()):
            if count[key] == max_value:
                return key


s = Solution()
print(s.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))
print(s.mostCommonWord("a.", []))