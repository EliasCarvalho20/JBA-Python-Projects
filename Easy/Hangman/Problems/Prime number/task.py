n = int(input())
tot = 0
for i in range(1, n + 1):
    if n % i == 0:
        tot += 1
if tot == 2:
    print('This number is prime')
else:
    print('This number is not prime')