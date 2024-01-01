import math

n = input()
numbers = [0 for _ in range(9)]

for i in range(len(n)):
    idx = 6 if int(n[i]) == 9 else int(n[i])
    numbers[idx] += 1

numbers[6] = math.ceil(numbers[6]/2) 
print(max(numbers))
    
############## 다른 풀이

n = int(input())
numbers = [0 for _ in range(10)]

while(n>0):
    numbers[n%10]+=1
    n = n//10

ans=-1
for i in range(10):
    if(i==6 or i==9): continue
    ans = max(ans,numbers[i])


print(max(ans, (numbers[6]+numbers[9]+1)//2))
