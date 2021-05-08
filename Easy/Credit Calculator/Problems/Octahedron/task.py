from math import sqrt, pow
n = int(input())
area = 2 * pow(n, 2) * sqrt(3)
volume = sqrt(2) / 3 * pow(n, 3)
print(f"{area:.2f} {volume:.2f}")
