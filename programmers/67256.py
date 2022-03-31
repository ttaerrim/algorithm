# [카카오 인턴] 키패드 누르기
def whichFinger(left, right, num, hand):
    distance = [0, 1, 2, 1, 2, 3, 2, 3, 4, 3, 4, 5]
    left_to_num = distance[abs(left-num)]
    right_to_num = distance[abs(right-num)]

    if left_to_num == right_to_num:
        return "R" if hand == "right" else "L"
    elif left_to_num < right_to_num:
        return "L"
    else:
        return "R"


def solution(numbers, hand):
    answer = ''
    left_finger, right_finger = 10, 12
    for num in numbers:
        if num == 0:
            num = 11
        if num == 1 or num == 4 or num == 7:
            answer += "L"
            left_finger = num
        elif num == 3 or num == 6 or num == 9:
            answer += "R"
            right_finger = num
        else:
            finger = whichFinger(left_finger, right_finger, num, hand)
            answer += finger
            if finger == "R":
                right_finger = num
            else:
                left_finger = num

    return answer
