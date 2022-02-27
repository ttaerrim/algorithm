num_array = list(map(int, input().split(" ")))
num_array.sort()
for i in range(len(num_array)):

    print(num_array[i], end=" ")
