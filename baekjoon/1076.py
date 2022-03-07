# 저항
color = ['black', 'brown', 'red', 'orange', 'yellow',
         'green', 'blue', 'violet', 'grey', 'white']
first, second, third = [color.index(input()) for i in range(3)]

print((first*10+second)*10**third)
