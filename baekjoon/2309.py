dwarfs = []
for i in range(9):
    dwarfs.append(int(input()))

diff = sum(dwarfs) - 100

innerBreak = True
firstDwarf = -1
secondDwarf = -1
for i in range(9):
    for j in range(8-i):
        if(dwarfs[i] + dwarfs[i+j+1] == diff):
            firstDwarf = dwarfs[i] 
            secondDwarf = dwarfs[i+j+1]
            innerBreak = False
            break
    if (innerBreak == False):
        break

dwarfs.remove(firstDwarf)
dwarfs.remove(secondDwarf)

for i in range(len(dwarfs)):
    print(sorted(dwarfs)[i])
