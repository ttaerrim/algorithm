# 손익분기점

import math

fix, variable, price= map(int, input().split(" "))
    
if (price <= variable):
    print(-1)
else:
    print(int(math.floor(fix /(price-variable)+1)))
        