n = int(input())
r = int(input())
t = 0
while r < n:
    n /= 2
    r += 1
    t += 12
print(t)