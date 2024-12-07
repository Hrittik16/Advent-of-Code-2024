def f(a: list, idx: int, ans: int, o: str):
    n = len(a)
    if o == "":
        ans *= int(a[idx])
    elif o == "|":
        ans = int(str(ans)+a[idx])
    elif o == "+":
        ans += int(a[idx])
    elif o == "*":
        ans *= int(a[idx])
    if idx == n-1:
        if ans == int(a[0]):
            return 1
        else:
            return 0
    k1 = f(a, idx+1, ans, "+")
    k2 = f(a, idx+1, ans, "*")
    k3 = f(a, idx+1, ans, "|")
    return k1 or k2 or k3

data = []
total = 0
with open('day7_data.txt', 'r') as file:
    for line in file:
        l = line.split()
        l[0] = l[0][:-1]
        data.append(l)
for line in data:
    if f(line, 1, 1, ""):
        total += int(line[0])
print(total)
