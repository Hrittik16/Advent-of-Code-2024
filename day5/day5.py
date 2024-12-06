d1 = {}
total = 0
with open('test_data_01.txt', 'r') as file:
    for line in file:
        a, b = [int(i) for i in line.split('|')]
        if a not in d1:
            d1[a] = [b]
        else:
            d1[a].append(b)
file.close()
with open('test_data_02.txt', 'r') as file:
    for line in file:
        l = [int(i) for i in line.split(',')]
        flag = 1
        d2 = {}
        for i in l:
            if i not in d1:
                d2[i] = 1
                continue
            for j in d1[i]:
                if j in d2:
                    flag = 0
                    break
            if not flag:
                break
            d2[i] = 1
        if flag: 
            total += l[len(l)//2]
print(total)
