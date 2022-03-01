# 방학 숙제
import math 
import sys

data = [int(sys.stdin.readline().strip()) for i in range(5)]

kr_hw_day = 1 if data[1] < data[3] else math.ceil(data[1] / data[3])
math_hw_day = 1 if data[2] < data[4] else math.ceil(data[2] / data[4])

print(data[0] - max(kr_hw_day, math_hw_day))