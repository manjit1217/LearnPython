l=['.......',
   '...O...',
   '....O..',
   '.......',
   'OO.....',
   'OO.....']

1
2
3

print(list(l[1]))
print(l[1][:4])
def bomberman(grid,r,c):
    grid1=[]
    for i in range(r):
        x=[]
        for j in range(c):
            x.append(('O'))
        grid1.append(x)

    for i in range(0,r-1):
        for j in range(0,c):
            if grid[i][j] == 'O':
                if i >0:
                    grid1[i][j]='.'
                    grid1[i-1][j]='.'
                    grid1[i+1][j]='.'
                    grid1[i][j+1]='.'
                    grid1[i][j-1]='.'
    for i in range(0,len(grid1)):
        print(''.join(grid1[i]))
bomberman(l,6,7)

