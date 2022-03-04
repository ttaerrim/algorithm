# 이상한 곱셈

def numToList(num):
    a=[]
    while(num!=0):
        a.append(num%10)
        num = num//10
    return list(reversed(a))

a, b = list(map(int, input().split()))
a_list, b_list = numToList(a), numToList(b)

print(sum(a_list)*sum(b_list))

