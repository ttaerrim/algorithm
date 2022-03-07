# 저항
import math


color = {'black': 1, 'brown': 10, 'red': 100, 'orange': 1000, 'yellow': 10000,
         'green': 100000, 'blue': 1000000, 'violet': 10000000, 'grey': 100000000, 'white': 1000000000}
first_color = input()
second_color = input()
third_color = input()

print((int(math.log10(color[first_color])) *
      10+int(math.log10(color[second_color])))*color[third_color])
