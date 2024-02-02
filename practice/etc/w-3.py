import random
def rand7():
    return random.randint(1, 7)

def rand5():
    while True:
        num = rand7()
        if num <= 5:
            return num

print(rand5())
