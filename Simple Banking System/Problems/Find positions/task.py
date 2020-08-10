numbers = input().split()
x = input()

if x not in numbers:
    print("not found")
else:
    for i, v in enumerate(numbers):
        if x == v:
            print(i, end=' ')
