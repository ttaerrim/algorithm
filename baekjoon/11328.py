n = int(input())
flag = False
for i in range(n):
    alpha = [0 for _ in range(26)]
    str1, str2 = map(str, input().split())
    if(len(str1)!=len(str2)):
        print('Impossible')
        continue
    for j in str1:
        idx1 = ord(j) - 97
        alpha[idx1] += 1
    for k in str2:
        idx2 = ord(k) - 97
        if(alpha[idx2] == 0):
            print('Impossible')
            flag = True
            break
        alpha[idx2] -= 1
    if(flag):
        flag = False
        continue
    else:
        print('Possible')

# 첫 번째 단어는 조회하며 알파벳 배열에서 1을 더하고
# 두 번째 단어는 조회하며 알파벳 배열에서 1을 뺀다
        
n = int(input())
flag = False
for i in range(n):
    alpha = [0 for _ in range(26)]
    str1, str2 = map(str, input().split())
    for j in str1:
        idx1 = ord(j) - 97
        alpha[idx1] += 1
    for k in str2:
        idx2 = ord(k) - 97
        alpha[idx2] -= 1

    if (alpha.count(0) == 26):
        print('Possible')
    else:
        print('Impossible')
