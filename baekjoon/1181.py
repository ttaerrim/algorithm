# 단어 정렬
import sys
n = int(sys.stdin.readline())
data = list(set([sys.stdin.readline().strip() for i in range(n)]))
data.sort(key=lambda x: (len(x), x.split()[0]))
for item in data:
    print(item)
