import sys
def main():
    n = int(sys.stdin.readline())
    stack = []
    for _ in range(n):
        c = sys.stdin.readline().split()
        if(c[0] == 'push'):
            stack.append(c[1])
        elif(c[0]=='pop'):
            if(len(stack)==0):
                print(-1)
            else:
                print(stack.pop())
        elif(c[0]=='size'):
            print(len(stack))
        elif(c[0]=='empty'):
            if(len(stack)==0):
                print(1)
            else:
                print(0)
        elif(c[0]=='top'):
            if(len(stack)!=0):
                print(stack[-1])
            else:
                print(-1)

main()
