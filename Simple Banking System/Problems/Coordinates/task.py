x, y = float(input()), float(input())

if x < 0:
    if y < 0:
        print('III')
    elif y > 0:
        print('II')
elif x > 0:
    if y > 0:
        print('I')
    else:
        print('IV')