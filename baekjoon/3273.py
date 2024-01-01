n = int(input())
lists = list(map(int, input().split()))
x = int(input())

nums = [0 for _ in range(1000000)]

answer = 0
for i in range(n):
    nums[lists[i]-1] = 1
    if(x - lists[i] > 1 and x - lists[i] - 1 < 1000000 and nums[x - lists[i] - 1]): answer+=1

print(answer)

################ 다른 풀이

n = int(input())
lists = list(map(int, input().split()))
x = int(input())

# 각 자연수의 존재 여부를 저장하는 배열
# 아래에서 x-list[i]가 1000000보다 큰 경우를 예외처리하지 않고 배열을 최대 200만으로 잡아서 해결할 수 있다
nums = [0 for _ in range(2000001)]

answer = 0
for i in range(n):
    nums[lists[i]] = 1
    if(x - lists[i] > 1 and nums[x - lists[i]]): answer+=1

print(answer)
