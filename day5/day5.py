d1 = {}
total = 0
total2 = 0
with open('day5_data_01.txt', 'r') as file:
    for line in file:
        a, b = [int(i) for i in line.split('|')]
        if a not in d1:
            d1[a] = [b]
        else:
            d1[a].append(b)
file.close()
with open('day5_data_02.txt', 'r') as file:
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
        else:
            #print("Array",":",end=" ")
            #for i in l: print(i,end=" ")
            idx = {}
            for i in range(len(l)):
                num = l[i]
                index = i
                if num not in d1:
                    idx[num] = index
                    continue
                for item in d1[num]:
                    if item in idx:
                        if idx[item] < index:
                            temp = index
                            index = idx[item]
                            idx[item] = temp
                            l[idx[item]] = item
                l[index] = num
                idx[num] = index
            #print("\nNew Array",":",end=" ")
            #for i in l: print(i,end=" ")
            #print()
            total2 += l[len(l)//2]
print(total)
print(total2)
