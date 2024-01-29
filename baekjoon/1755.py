# https://www.acmicpc.net/problem/1755
# 숫자놀이

m, n = map(int, input().split(" "))
num2str = {}
number = {'0':'zero', '1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine'}

for num in range(m, n+1):
    strNum = str(num)
    temp = ''
    for s in strNum:
        temp += number[s]
    num2str[num] = temp

for i, item in enumerate(sorted(num2str.items(), key = lambda x:x[1])):
    print(item[0], end='\n' if i > 0 and i % 10 == 9 else " ")
