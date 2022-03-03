# 8진수 2진수
onum = input()

bnum = int(onum, 8)
bnum = bin(bnum)[2:]

print(bnum)