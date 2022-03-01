# TV 크기

diagonal, height, width= map(int, input().split(" "))

ratio = (diagonal**2 / (height**2 + width**2))**(1/2)
print(int(height*ratio), int(width*ratio))