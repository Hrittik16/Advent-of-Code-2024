g = []
with open('day6_data.txt', 'r') as file:
    for line in file:
        l = []
        for i in line: 
            if i == '\n': break
            l.append(i)
        g.append(l)
r = len(g)
c = len(g[0])

dir = ['^', '>', '+', '-']

i=0
j=0
for x in range(r):
    for y in range(c):
        if g[x][y] == '^':
            i = x
            j = y
curr = 0
flag = 0
count = 1
g[i][j] = '.'
vis = [[0]*c for i in range(r)]
vis[i][j] = 1
while(1):
    if dir[curr] == '^':
        while(i-1 >= 0 and g[i-1][j] == '.'):
            i -= 1
            if not vis[i][j]:
                count += 1
                vis[i][j] = 1
        if i == 0: flag = 1
        curr = (curr+1)%4
    elif dir[curr] == '>':
        while(j+1 < c and g[i][j+1] == '.'):
            j += 1
            if not vis[i][j]:
                count += 1
                vis[i][j] = 1
        if j == c-1: flag = 1
        curr = (curr+1)%4
    elif dir[curr] == '+':
        while(i+1 < r and g[i+1][j] == '.'):
            i += 1
            if not vis[i][j]:
                count += 1
                vis[i][j] = 1
        if i == r-1: flag = 1
        curr = (curr+1)%4
    elif dir[curr] == '-':
        while(j-1 >= 0 and g[i][j-1] == '.'):
            j -= 1
            if not vis[i][j]:
                count += 1
                vis[i][j] = 1
        if j == 0: flag = 1
        curr = (curr+1)%4
    if flag: break
print(count)
