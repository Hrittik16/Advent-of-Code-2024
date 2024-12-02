def report_safe(l: list):
    d = [x-y for x, y in zip(l, l[1:])]
    return all(1 <= x <= 3 for x in d) or all(-1 >= x >= -3 for x in d)
count = 0
count2 = 0
with open('day2_data.txt', 'r') as file:
    for line in file:
        report = [int(i) for i in line.split()]
        if report_safe(report): 
            count += 1
            count2 += 1
        else:
            for i in range(len(report)):
                new_report = report[:i]+report[i+1:]
                if report_safe(new_report): 
                    count2 += 1
                    break

print(count)
print(count2)
