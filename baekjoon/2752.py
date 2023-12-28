num_array = list(map(int, input().split(" ")))
num_array.sort()
for i in range(len(num_array)):

    print(num_array[i], end=" ")

#################### 다른 풀이 

a, b, c = map(int, input().split())
maxNum = max([a, b, c])
minNum = min([a, b, c])

def middle(array):
    for i in array:
        if (i != max(array) and i != min(array)):
            middle = i
    return middle


middle = middle([a, b, c])
print(minNum, middle, maxNum)

#################### 숏 코딩

print(*sorted(map(int, input().split())))

#################### 다른 풀이 2

a, b, c = map(int, input().split())
maxNum = max([a, b, c])
minNum = min([a, b, c])
middleNum = a + b + c - maxNum - minNum

print(minNum, middleNum, maxNum)
