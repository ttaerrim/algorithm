# 나누기 
num = input()
divisor = int(input())
new_num = int(num[:-2]+'00')

if (divisor - new_num%divisor)==divisor:
    print('00')
elif len(str(divisor - new_num%divisor))==1:
    print('0'+str(divisor - new_num%divisor))
else:
    print(divisor - new_num%divisor)