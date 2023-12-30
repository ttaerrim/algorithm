def createList(n):
    lst = []
    for i in range(1, n + 1):
        lst.append(i)
    return lst

def insert_position(position, list1, list2):
    return list1[:position] + list2 + list1[position:]

list = createList(20)

for i in range(10):
    a, b = map(int, input().split())
    tempArr = []
    for i in range(a-1, b):
        tempArr.append(list[i])
    tempArr.reverse()
    del list[a-1:b]
    list = insert_position(a-1, list, tempArr)

for i in range(len(list)):
    print(list[i], end=" ")
