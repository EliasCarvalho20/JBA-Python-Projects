n = int(input())
char = "#"
for x in range(n, 0, -1):
    print(f"{' ' * (x - 1)}{char}")
    char += "##"
