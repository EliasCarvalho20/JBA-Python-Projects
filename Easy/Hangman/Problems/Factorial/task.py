number = int(input())
counter = number
fator = 1
while counter > 0:
    fator *= counter
    counter -= 1
print(fator)