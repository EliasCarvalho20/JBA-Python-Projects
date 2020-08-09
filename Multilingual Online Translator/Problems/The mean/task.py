numbers = []
while True:
    user = input()
    if '.' in user:
        break
    numbers.append(int(user))
print(sum(numbers) / len(numbers))
