class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        digit, letter = [], []
        for log in logs:
            if log.split()[1].isdigit():
                digit.append(log)
            else:
                letter.append(log)
        
        letter.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        
        return letter+digit


s = Solution()
print(s.reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))
print(s.reorderLogFiles(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car"]))

        