import itertools

def solution(arr, add):
    flat_arr=list(itertools.chain(*arr))
    added_arr=sorted(list(set(flat_arr+add)))

    answer = []
    temp = []
    idx=0
    while idx < len(added_arr):
        num = added_arr[idx] 
        if idx == 0 or num - 1 in temp:
            temp.append(num)
            
        else:
            answer.append(temp)
            temp = [num]
        idx += 1

    if len(temp) != 0:
        answer.append(temp)
    
    print(answer)

    


solution([[1,2,3], [6, 7], [13]], [4, 5])
solution([[1,2,3], [6, 7], [13]], [3, 4, 5])
solution([[1,2,3], [6, 7], [13]], [7, 8, 9, 12])
solution([[1,2,3], [6, 7], [13]], [1,2,3,4,5,6,7,8,9,10,11,12,13])
