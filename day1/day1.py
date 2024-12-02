list1 = []
list2 = []
fre1 = {}
fre2 = {}
with open('day1_data.txt', 'r') as file:
    for line in file:
        x, y = [int(i) for i in line.split()]
        list1.append(x)
        list2.append(y)
        if x not in fre1: fre1[x] = 1
        else: fre1[x] += 1
        if y not in fre2: fre2[y] = 1
        else: fre2[y] += 1
# Task 1
list1 = sorted(list1)
list2 = sorted(list2)
dist = 0
for i in range(len(list1)):
    dist += abs(list1[i]-list2[i])

# Task2
similarity = 0
for item in list1:
    if item in fre2:
        similarity += item*fre2[item]

print(dist)
print(similarity)
