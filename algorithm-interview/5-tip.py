# 파이썬의 정렬 방법
my_list = [2, 5, 1, 9, 7]

my_list.sort()
print(my_list)
alist = my_list.sort() # 잘못된 구문. sort() 함수는 None을 리턴함.

c = ['ccc', 'aaaa', 'd', 'bb']
c_result = sorted(c, key=lambda x: len(x)) # key= 옵션으로 정렬 위한 키나 함수 별도 지정 가능
print(c_result)

# 함수를 이용해 키 정의하는 방법

a = ['cde', 'cfc', 'abc']
def fn(s):
    return s[0], s[-1]

print(sorted(a, key=fn))
print(sorted(a, key=lambda s: (s[0], s[-1])))