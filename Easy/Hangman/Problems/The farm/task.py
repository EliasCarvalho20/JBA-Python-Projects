cash = int(input())
total = 0
price = [23, 678, 1296, 3848, 6769]
animals = ['chicken', 'goat', 'pig', 'cow', 'sheep']
if cash < price[0]:
    print('None')
elif cash < price[1]:
    total = cash // price[0]
    print(f'{total} {animals[0]}' if total < 2 else f'{total} {animals[0]}s')
elif cash < price[2]:
    total = cash // price[1]
    print(f'{total} {animals[1]}' if total < 2 else f'{total} {animals[1]}s')
elif cash < price[3]:
    total = cash // price[2]
    print(f'{total} {animals[2]}' if total < 2 else f'{total} {animals[2]}s')
elif cash < price[4]:
    total = cash // price[3]
    print(f'{total} {animals[3]}' if total < 2 else f'{total} {animals[3]}s')
else:
    total = cash // price[4]
    print(f'{total} {animals[4]}')
