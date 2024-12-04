data = []
with open('day4_data.txt', 'r') as file:
    for line in file:
        data.append(line.strip())
n = len(data)
m = len(data[0])

count = 0

# horizontal 
for i in data:
    for j in range(m-3):
        s = i[j:j+4]
        ss = s[::-1]
        if s == 'XMAS': count += 1
        if ss == 'XMAS': count += 1

# vertical
for j in range(m):
    for i in range(n-3):
        s = ''
        for k in range(i, i+4):
            s += data[k][j]
        ss = s[::-1]
        if s == 'XMAS': count += 1
        if ss == 'XMAS': count += 1

# Diagonals
for i in range(n-3):
    for j in range(m-3):
        s = ''
        p = ''
        for k in range(4):
            s += data[i+k][j+k]
            p += data[i+k][m-(j+k)-1]
        ss = s[::-1]
        pp = p[::-1]
        if s == 'XMAS': count += 1
        if ss == 'XMAS': count += 1
        if p == 'XMAS': count += 1
        if pp == 'XMAS': count += 1

print(count)

count2 = 0

# X-MAS
for i in range(n-2):
    for j in range(m-2):
        l = data[i][j]+data[i+1][j+1]+data[i+2][j+2]
        r = data[i][j+2]+data[i+1][j+1]+data[i+2][j]
        if (l == 'MAS' or l == 'SAM') and (r == 'MAS' or r == 'SAM'):
            count2 += 1
print(count2)
