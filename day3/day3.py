import re
muls = []
new_muls = []
flag = 1
with open('day3_data.txt', 'r') as file:
    for line in file:
        x = re.findall(r"mul\([0-9]+,[0-9]+\)|do\(\)|don\'t\(\)", line)
        for i in x:
            if i == "don't()":
                if flag:
                    flag = 0
                continue
            if i == "do()":
                if not flag:
                    flag = 1
                continue
            muls.append(i)
            if flag: 
                new_muls.append(i)
total = 0
total2 = 0
for i in muls:
    m = re.findall(r'\d+', i)
    total += int(m[0])*int(m[1])
for i in new_muls:
    m = re.findall(r'\d+', i)
    total2 += int(m[0])*int(m[1])
print(total)
print(total2)
