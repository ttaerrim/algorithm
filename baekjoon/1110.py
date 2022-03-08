# 더하기 사이클

initial_number = input()
number = '0' + initial_number if int(initial_number) < 10 else initial_number
count = 0

while True:
    number = number[1]+str(int(number[0])+int(number[1]))[-1]
    count += 1
    if (int(number) == int(initial_number)):
        break

print(count)
