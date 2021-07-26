import collections

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams=collections.defaultdict(list) #defaultdict을 사용하면 없는 key에 변수를 추가할 때 keyerror 방지할 수 있다.

        for word in strs:
            key = ''.join(sorted(word)) #단어를 정렬한 다음 join으로 문자열로 만든다.
            anagrams[key].append(word)
        
        return anagrams.values()